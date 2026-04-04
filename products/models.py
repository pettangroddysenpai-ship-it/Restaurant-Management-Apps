from django.db import models
# Create your models here.
class Ingredient(models.Model):
    id_ingredient = models.AutoField(primary_key=True, db_column='id_Ingredient')
    nom = models.CharField(max_length=45, db_column='Nom')
    unite_de_mesure = models.CharField(max_length=45, db_column='Unite_de_Mesure')
    type = models.CharField(max_length=30, db_column='Type')
    class Meta:
        managed = False
        db_table = 'Ingredient'
    def __str__(self): return self.nom

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True, db_column='id_Produit')
    id_createur = models.ForeignKey('hr.Employe', on_delete=models.SET_NULL, null=True, db_column='id_Createur')
    nom = models.CharField(max_length=30, db_column='Nom')
    description = models.CharField(max_length=45, db_column='Description')
    duree_cuisson = models.CharField(max_length=20, db_column='Duree_Cuisson')
    nombre_personnes = models.IntegerField(db_column='Nombre_Personnes')
    class Meta:
        managed = False
        db_table = 'Produit'
    def __str__(self): return self.nom

class CompositionProduit(models.Model):
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE, db_column='id_Produit')
    id_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='id_Ingredient')
    quantite_utilisee = models.DecimalField(max_digits=10, decimal_places=2, db_column='Quantite_Utilisee')
    class Meta:
        managed = False
        db_table = 'Composition_Produit'
        unique_together = [('id_produit', 'id_ingredient')]

