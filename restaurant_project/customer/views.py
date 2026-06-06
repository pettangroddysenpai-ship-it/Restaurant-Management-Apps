from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from orders.models import Commande, LigneCommande, Client
from inventory.models import Stock, VariationStock
from products.models import Produit, CompositionProduit
from django.utils import timezone
from decimal import Decimal

IMAGE_MAP = {
    'Poulet DG': 'Poulet DG.PNG',
    'Ndol\u251c\u00ae': 'Ndole.PNG',
    'Riz saut\u251c\u00ae': 'Riz saute.PNG',
    'Jus de Gingembre': 'Jus de Jingembre.PNG',
    'Jus de Bissap': 'Jus de Bissap.PNG',
}

def menu(request):
    products = Produit.objects.all()
    product_data = []
    for p in products:
        last_line = LigneCommande.objects.filter(
            id_produit=p.pk
        ).order_by('-id_commande').first()
        prix = last_line.prix_unitaire if last_line else 0

        compositions = CompositionProduit.objects.filter(id_produit=p.pk)
        portions = None
        for comp in compositions:
            try:
                stock = Stock.objects.get(id_ingredient=comp.id_ingredient)
                if comp.quantite_utilisee > 0:
                    possible = int(stock.quantite_actuelle / comp.quantite_utilisee)
                    if portions is None or possible < portions:
                        portions = possible
            except Stock.DoesNotExist:
                portions = 0
                break
        if portions is None:
            portions = 0

        img_file = IMAGE_MAP.get(p.nom, '')

        product_data.append({
            'id': p.pk,
            'nom': p.nom,
            'description': p.description,
            'prix': prix,
            'portions_disponibles': portions,
            'img_file': img_file,
        })

    return render(request, 'customer/menu.html', {'products': product_data})


def order_create(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name', '').strip()
        if not client_name:
            messages.error(request, 'Please enter your name.')
            return redirect('customer:order')

        name_parts = client_name.split(' ', 1)
        prenom = name_parts[0]
        nom = name_parts[1] if len(name_parts) > 1 else ''

        client, created = Client.objects.get_or_create(
            nom=nom,
            prenom=prenom,
            defaults={'tel': '', 'email': '', 'type_de_client': 'Particulier'}
        )

        commande = Commande.objects.create(
            id_client=client,
            date=timezone.now(),
            type=request.POST.get('type', 'Sur place'),
            montant_total=0,
            mode_de_paiement=request.POST.get('paiement', 'Esp\u00e8ces'),
        )

        total = 0
        for produit_id, qty, prix in zip(
            request.POST.getlist('produit_id'),
            request.POST.getlist('quantite'),
            request.POST.getlist('prix_unitaire')
        ):
            if not produit_id or not qty or not prix:
                continue
            LigneCommande.objects.create(
                id_commande=commande.pk, id_produit_id=produit_id,
                quantite=qty, prix_unitaire=int(prix)
            )
            total += float(prix) * float(qty)
            deduct_stock_for_product(produit_id, Decimal(qty))

        commande.montant_total = int(total)
        commande.save()

        messages.success(request, f'Order #{commande.pk} created! Total: {int(total)} FCFA')
        return redirect('customer:order_success', pk=commande.pk)

    produits = Produit.objects.all()
    product_data = []
    for produit in produits:
        last_line = LigneCommande.objects.filter(
            id_produit=produit.pk
        ).order_by('-id_commande').first()
        prix = last_line.prix_unitaire if last_line else 0

        compositions = CompositionProduit.objects.filter(id_produit=produit.pk)
        portions = None
        for comp in compositions:
            try:
                stock = Stock.objects.get(id_ingredient=comp.id_ingredient)
                if comp.quantite_utilisee > 0:
                    possible = int(stock.quantite_actuelle / comp.quantite_utilisee)
                    if portions is None or possible < portions:
                        portions = possible
            except Stock.DoesNotExist:
                portions = 0
                break
        if portions is None:
            portions = 0

        product_data.append({
            'id': produit.pk,
            'nom': produit.nom,
            'prix': prix,
            'portions_disponibles': portions,
        })

    return render(request, 'customer/order.html', {'product_data': product_data})


def order_success(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    lignes = LigneCommande.objects.filter(id_commande=pk)
    return render(request, 'customer/order_success.html', {
        'commande': commande,
        'lignes': lignes,
    })


def deduct_stock_for_product(produit_id, qty_ordered):
    qty_ordered = Decimal(str(qty_ordered))
    compositions = CompositionProduit.objects.filter(id_produit_id=produit_id)
    for comp in compositions:
        stock = Stock.objects.get(id_ingredient=comp.id_ingredient)
        qty_used = comp.quantite_utilisee * qty_ordered
        stock.quantite_actuelle -= qty_used
        stock.save()
        VariationStock.objects.create(
            id_ingredient=comp.id_ingredient,
            date=timezone.now().date(),
            type='sortie',
            quantite=qty_used
        )
