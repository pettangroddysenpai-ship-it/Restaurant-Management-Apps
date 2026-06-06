"""
URL configuration for restaurant_project project.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('inventory/', include('inventory.urls')),
    path('hr/', include('hr.urls')),
    path('delivery/', include('delivery.urls')),
    path('finance/', include('finance.urls')),
    path('customer/', include('customer.urls')),
]
