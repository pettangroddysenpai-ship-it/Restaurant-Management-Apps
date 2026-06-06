from django.db import models

class Vehicule(models.Model):
    id_vehicule = models.AutoField(primary_key=True, db_column='id_Vehicule')
    immatriculation = models.CharField(max_length=15, db_column='Immatriculation')
    modele = models.CharField(max_length=20, db_column='Modele')
    marque = models.CharField(max_length=20, db_column='Marque')
    class Meta:
        managed = False
        db_table = 'Vehicule'
    def __str__(self): return f'{self.marque} {self.modele} ({self.immatriculation})'

class Deplacement(models.Model):
    id_deplacement = models.AutoField(primary_key=True, db_column='id_Deplacement')
    id_chauffeur = models.IntegerField(db_column='id_Chauffeur')
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, db_column='id_Vehicule')
    date_depart = models.DateTimeField(db_column='Date_depart')
    destination = models.TextField(db_column='Destination')
    distance_totale = models.DecimalField(max_digits=10, decimal_places=2, db_column='Distance_totale')
    class Meta:
        managed = False
        db_table = 'Deplacement'
    def __str__(self): return f'Déplacement #{self.id_deplacement}'

class Livraison(models.Model):
    id_livraison = models.AutoField(primary_key=True, db_column='id_Livraison')
    id_commande = models.ForeignKey('orders.Commande', on_delete=models.CASCADE, db_column='id_Commande')
    id_deplacement = models.ForeignKey(Deplacement, on_delete=models.CASCADE, db_column='id_Deplacement')
    class Meta:
        managed = False
        db_table = 'Livraison'
    def __str__(self): return f'Livraison #{self.id_livraison}'
