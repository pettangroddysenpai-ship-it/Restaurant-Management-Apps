from django.db import models

class Stock(models.Model):
    id_ingredient = models.OneToOneField('products.Ingredient', primary_key=True, on_delete=models.CASCADE, db_column='id_Ingredient')
    quantite_actuelle = models.DecimalField(max_digits=10, decimal_places=2, db_column='Quantite_Actuelle')
    seuil_alerte = models.DecimalField(max_digits=10, decimal_places=2, db_column='Seuil_Alerte')
    class Meta:
        managed = False
        db_table = 'Stock'
    def __str__(self): return f'Stock {self.id_ingredient}'

class VariationStock(models.Model):
    id_variation = models.AutoField(primary_key=True, db_column='id_Variation')
    id_ingredient = models.ForeignKey('products.Ingredient', on_delete=models.CASCADE, db_column='id_Ingredient')
    date = models.DateField(db_column='Date')
    type = models.CharField(max_length=20, db_column='Type')
    quantite = models.DecimalField(max_digits=10, decimal_places=2, db_column='Quantite')
    class Meta:
        managed = False
        db_table = 'Variation_Stock'
