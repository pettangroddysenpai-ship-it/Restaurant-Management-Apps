from django.contrib import admin
from .models import Livraison, Deplacement, Vehicule

admin.site.register(Livraison)
admin.site.register(Deplacement)
admin.site.register(Vehicule)
