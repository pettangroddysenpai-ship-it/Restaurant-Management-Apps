from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F
from django.utils import timezone
from orders.models import Commande, LigneCommande
from products.models import Produit
from inventory.models import Stock
import datetime

@login_required
def index(request):
    today = timezone.now()
    current_month = today.month
    current_year = today.year

    monthly_revenue = Commande.objects.filter(
        date__month=current_month, date__year=current_year
    ).aggregate(total=Sum('montant_total'))['total'] or 0

    order_count = Commande.objects.filter(
        date__month=current_month, date__year=current_year
    ).count()

    best_sellers = LigneCommande.objects.values(
        'id_produit__nom'
    ).annotate(total_sold=Sum('quantite')).order_by('-total_sold')[:5]

    low_stock = Stock.objects.filter(quantite_actuelle__lte=F('seuil_alerte'))

    monthly_data = []
    for i in range(5, -1, -1):
        month = today - datetime.timedelta(days=30*i)
        rev = Commande.objects.filter(
            date__month=month.month, date__year=month.year
        ).aggregate(total=Sum('montant_total'))['total'] or 0
        monthly_data.append({'month': month.strftime('%b %Y'), 'revenue': rev})

    recent_orders = Commande.objects.all().order_by('-date')[:5]
    total_products = Produit.objects.count()

    context = {
        'monthly_revenue': monthly_revenue,
        'order_count': order_count,
        'best_sellers': best_sellers,
        'low_stock': low_stock,
        'monthly_data': monthly_data,
        'recent_orders': recent_orders,
        'total_products': total_products,
    }
    return render(request, 'dashboard/index.html', context)
