from django.contrib import admin
from .models import Commande, LigneCommande, Client, Reservation, TableRestaurant

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id_commande', 'id_client', 'date', 'type', 'montant_total', 'mode_de_paiement']
    list_filter = ['type', 'mode_de_paiement']
    search_fields = ['id_commande', 'id_client__nom']
    ordering = ['-date']

admin.site.register(Client)
admin.site.register(LigneCommande)
admin.site.register(Reservation)
admin.site.register(TableRestaurant)
