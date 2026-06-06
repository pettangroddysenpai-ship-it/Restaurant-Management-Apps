from django.db import models

class Facture(models.Model):
    id_facture = models.AutoField(primary_key=True, db_column='id_Facture')
    date = models.DateField(db_column='Date')
    montant = models.IntegerField(db_column='Montant')
    type = models.CharField(max_length=45, db_column='Type')
    class Meta:
        managed = False
        db_table = 'Facture'
    def __str__(self):
        return f'Facture #{self.id_facture} - {self.montant} FCFA'
