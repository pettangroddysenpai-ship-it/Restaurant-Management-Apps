from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Livraison, Deplacement, Vehicule
from hr.models import Employe

@login_required
def delivery_list(request):
    deliveries = Livraison.objects.select_related('id_commande', 'id_deplacement__id_vehicule').all()
    deplacements = Deplacement.objects.select_related('id_vehicule').all()

    chauffeur_ids = set()
    for d in deplacements:
        chauffeur_ids.add(d.id_chauffeur)
    for liv in deliveries:
        chauffeur_ids.add(liv.id_deplacement.id_chauffeur)

    chauffeurs = Employe.objects.filter(id_employe__in=chauffeur_ids)
    chauffeur_map = {c.id_employe: f'{c.prenom} {c.nom}' for c in chauffeurs}

    delivery_data = []
    for liv in deliveries:
        dep = liv.id_deplacement
        chauffeur_name = chauffeur_map.get(dep.id_chauffeur, 'Inconnu')
        delivery_data.append({
            'id': liv.id_livraison,
            'commande_id': liv.id_commande.id_commande,
            'chauffeur': chauffeur_name,
            'vehicule': f'{dep.id_vehicule.marque} {dep.id_vehicule.modele}',
            'destination': dep.destination,
            'date_depart': dep.date_depart,
        })

    deplacement_data = []
    for d in deplacements:
        chauffeur_name = chauffeur_map.get(d.id_chauffeur, 'Inconnu')
        deplacement_data.append({
            'id': d.id_deplacement,
            'chauffeur': chauffeur_name,
            'vehicule': f'{d.id_vehicule.marque} {d.id_vehicule.modele} ({d.id_vehicule.immatriculation})',
            'destination': d.destination,
            'distance': d.distance_totale,
            'date_depart': d.date_depart,
        })

    context = {
        'delivery_data': delivery_data,
        'deplacement_data': deplacement_data,
    }
    return render(request, 'delivery/list.html', context)
