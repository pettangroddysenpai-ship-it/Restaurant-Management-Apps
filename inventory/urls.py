# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('',           views.order_list,   name='list'),
    path('<int:pk>/',  views.order_detail, name='detail'),
    path('new/',       views.order_create, name='create'),
]

# restaurant_project/urls.py  (main router)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',     admin.site.urls),
    path('accounts/', include('users.urls')),
    path('orders/',   include('orders.urls')),
    path('products/', include('products.urls')),
    path('inventory/',include('inventory.urls')),
    path('hr/',       include('hr.urls')),
    path('delivery/', include('delivery.urls')),
    path('finance/',  include('finance.urls')),
    path('',          include('dashboard.urls')),
]
