# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Commande, LigneCommande, Client
from inventory.models import Stock, VariationStock
from products.models import CompositionProduit
import datetime

@login_required
def order_list(request):
    commandes = Commande.objects.all().order_by('-date')
    return render(request, 'orders/list.html', {'commandes': commandes})

@login_required
def order_detail(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    lignes = LigneCommande.objects.filter(id_commande=commande)
    return render(request, 'orders/detail.html', {'commande': commande, 'lignes': lignes})

@login_required
def order_create(request):
    if request.method == 'POST':
        # 1. Create the order
        commande = Commande.objects.create(
            id_client_id=request.POST['client_id'],
            date=datetime.datetime.now(),
            type=request.POST['type'],
            montant_total=0,
            mode_de_paiement=request.POST['paiement'],
        )
        total = 0
        # 2. Add each line item
        for produit_id, qty in zip(request.POST.getlist('produit_id'), request.POST.getlist('quantite')):
            prix = int(request.POST.get(f'prix_{produit_id}', 0))
            LigneCommande.objects.create(
                id_commande=commande, id_produit_id=produit_id,
                quantite=qty, prix_unitaire=prix
            )
            total += prix * float(qty)
            # 3. Deduct ingredients from Stock automatically
            deduct_stock_for_product(produit_id, float(qty))
        # 4. Update total
        commande.montant_total = int(total)
        commande.save()
        messages.success(request, 'Commande créée avec succès!')
        return redirect('orders:detail', pk=commande.pk)
    clients = Client.objects.all()
    return render(request, 'orders/create.html', {'clients': clients})

def deduct_stock_for_product(produit_id, qty_ordered):
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
            date=datetime.date.today(),
            type='sortie',
            quantite=qty_used
        )
