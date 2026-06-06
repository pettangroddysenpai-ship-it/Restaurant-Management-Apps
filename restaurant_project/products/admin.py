from django.contrib import admin
from .models import Produit, Ingredient, CompositionProduit

admin.site.register(Produit)
admin.site.register(Ingredient)
admin.site.register(CompositionProduit)
