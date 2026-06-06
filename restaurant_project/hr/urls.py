from django.urls import path
from . import views

app_name = 'hr'
urlpatterns = [
    path('', views.employee_list, name='list'),
]
