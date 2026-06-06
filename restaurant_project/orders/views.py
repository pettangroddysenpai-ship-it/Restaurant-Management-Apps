# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Commande, LigneCommande, Client
from inventory.models import Stock, VariationStock
from products.models import Produit, CompositionProduit
from django.utils import timezone
from decimal import Decimal

@login_required
def order_list(request):
    commandes = Commande.objects.all().order_by('-date')
    return render(request, 'orders/list.html', {'commandes': commandes})

@login_required
def order_detail(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    lignes = LigneCommande.objects.filter(id_commande=commande.pk)
    return render(request, 'orders/detail.html', {'commande': commande, 'lignes': lignes})

@login_required
def order_create(request):
    if request.method == 'POST':
        # 1. Create the order
        commande = Commande.objects.create(
            id_client_id=request.POST['client_id'],
            date=timezone.now(),
            type=request.POST['type'],
            montant_total=0,
            mode_de_paiement=request.POST['paiement'],
        )
        total = 0
        # 2. Add each line item
        for produit_id, qty, prix in zip(
            request.POST.getlist('produit_id'),
            request.POST.getlist('quantite'),
            request.POST.getlist('prix_unitaire')
        ):
            LigneCommande.objects.create(
                id_commande=commande.pk, id_produit_id=produit_id,
                quantite=qty, prix_unitaire=int(prix)
            )
            total += float(prix) * float(qty)
            # 3. Deduct ingredients from Stock automatically
            deduct_stock_for_product(produit_id, Decimal(qty))
        # 4. Update total
        commande.montant_total = int(total)
        commande.save()
        messages.success(request, 'Order created successfully!')
        return redirect('orders:detail', pk=commande.pk)
    clients = Client.objects.all()

    # Build product list enriched with price and available stock
    produits = Produit.objects.all()
    product_data = []
    for produit in produits:
        # Get most recent unit price from order history
        last_line = LigneCommande.objects.filter(
            id_produit=produit.pk
        ).order_by('-id_commande').first()
        prix = last_line.prix_unitaire if last_line else 0

        # Compute how many portions can be made from current stock
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

    return render(request, 'orders/create.html', {
        'clients': clients,
        'product_data': product_data,
    })

def deduct_stock_for_product(produit_id, qty_ordered):
    qty_ordered = Decimal(str(qty_ordered))
    '''Automatically reduce stock when an order is placed'''
    compositions = CompositionProduit.objects.filter(id_produit_id=produit_id)
    for comp in compositions:
        stock = Stock.objects.get(id_ingredient=comp.id_ingredient)
        qty_used = comp.quantite_utilisee * qty_ordered
        stock.quantite_actuelle -= qty_used
        stock.save()
        # Log the variation
        VariationStock.objects.create(
            id_ingredient=comp.id_ingredient,
            date=timezone.now().date(),
            type='sortie',
            quantite=qty_used
        )
