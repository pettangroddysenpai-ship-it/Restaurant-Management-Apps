from django.db import models

# Create your models here.
class Client(models.Model):
    id_client = models.AutoField(primary_key=True, db_column='id_Client')
    nom = models.CharField(max_length=20, db_column='Nom')
    prenom = models.CharField(max_length=20, db_column='Prenom')
    tel = models.CharField(max_length=15, db_column='Tel')
    email = models.CharField(max_length=45, db_column='Email')
    type_de_client = models.CharField(max_length=20, db_column='Type_de_Client')
    class Meta:
        managed = False
        db_table = 'Client'
    def __str__(self):
        return f'{self.prenom} {self.nom}'

class TableRestaurant(models.Model):   # 'Table' is a reserved word!
    id_table = models.AutoField(primary_key=True, db_column='id_Table')
    numero_table = models.CharField(max_length=3, db_column='Numero_Table')
    capacite = models.IntegerField(db_column='Capacite')
    commentaire = models.TextField(db_column='Commentaire', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Table'
    def __str__(self):
        return f'Table {self.numero_table}'

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True, db_column='id_Reservation')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='id_Client')
    id_table = models.ForeignKey(TableRestaurant, on_delete=models.CASCADE, db_column='id_Table')
    date = models.DateField(db_column='Date')
    heure = models.TimeField(db_column='Heure')
    statut = models.CharField(max_length=45, db_column='Statut')
    class Meta:
        managed = False
        db_table = 'Reservation'

class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True, db_column='id_Commande')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='id_Client')
    date = models.DateTimeField(db_column='Date')
    type = models.CharField(max_length=30, db_column='Type')
    montant_total = models.IntegerField(db_column='Montant_Total')
    mode_de_paiement = models.CharField(max_length=45, db_column='Mode_de_Paiement')
    class Meta:
        managed = False
        db_table = 'Commande'
    def __str__(self):
        return f'Commande #{self.id_commande}'

class LigneCommande(models.Model):
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE, db_column='id_Commande')
    id_produit = models.ForeignKey('products.Produit', on_delete=models.CASCADE, db_column='id_Produit')
    quantite = models.DecimalField(max_digits=10, decimal_places=2, db_column='Quantite')
    prix_unitaire = models.IntegerField(db_column='Prix_Unitaire')
    class Meta:
        managed = False
        db_table = 'Ligne_Commande'
        unique_together = [('id_commande', 'id_produit')]

