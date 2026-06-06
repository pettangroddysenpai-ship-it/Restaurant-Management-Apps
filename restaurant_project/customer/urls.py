from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('order/', views.order_create, name='order'),
    path('order/success/<int:pk>/', views.order_success, name='order_success'),
]
