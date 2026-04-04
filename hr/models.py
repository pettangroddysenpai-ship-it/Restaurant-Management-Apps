from django.db import models

# Create your models here.
class Affectation(models.Model):
    id_employe = models.ForeignKey('Employe', on_delete=models.CASCADE, db_column='id_Employe')
    id_poste = models.ForeignKey('Poste', on_delete=models.CASCADE, db_column='id_Poste')
    date_debut = models.DateField(db_column='Date_debut')
    date_fin = models.DateField(db_column='Date_fin', null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'Affectation'
        unique_together = [('id_employe', 'id_poste')]  # composite PK

