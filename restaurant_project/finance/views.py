from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
from orders.models import Commande
import datetime

@login_required
def finance_dashboard(request):
    today = timezone.now()
    current_month = today.month
    current_year = today.year

    monthly_revenue = Commande.objects.filter(
        date__month=current_month, date__year=current_year
    ).aggregate(total=Sum('montant_total'))['total'] or 0

    order_count = Commande.objects.filter(
        date__month=current_month, date__year=current_year
    ).count()

    monthly_data = []
    for i in range(5, -1, -1):
        month = today - datetime.timedelta(days=30*i)
        rev = Commande.objects.filter(
            date__month=month.month, date__year=month.year
        ).aggregate(total=Sum('montant_total'))['total'] or 0
        monthly_data.append({'month': month.strftime('%b %Y'), 'revenue': rev})

    context = {
        'monthly_revenue': monthly_revenue,
        'order_count': order_count,
        'monthly_data': monthly_data,
    }
    return render(request, 'finance/dashboard.html', context)
