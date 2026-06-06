from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Stock

@login_required
def stock_list(request):
    stocks = Stock.objects.select_related('id_ingredient').all()
    return render(request, 'inventory/list.html', {'stocks': stocks})

@login_required
def stock_alerts(request):
    low_stock = Stock.objects.filter(
        quantite_actuelle__lte=F('seuil_alerte')
    ).select_related('id_ingredient')
    return render(request, 'inventory/alerts.html', {'low_stock': low_stock})
