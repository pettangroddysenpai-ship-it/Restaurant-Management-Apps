from django.db import models

class Employe(models.Model):
    id_employe = models.AutoField(primary_key=True, db_column='id_Employe')
    nom = models.CharField(max_length=20, db_column='Nom')
    prenom = models.CharField(max_length=20, db_column='Prenom')
    tel = models.CharField(max_length=15, db_column='Tel')
    salaire = models.IntegerField(db_column='Salaire')
    date_embauche = models.DateField(db_column='Date_Embauche')
    class Meta:
        managed = False
        db_table = 'Employe'
    def __str__(self): return f'{self.prenom} {self.nom}'

class Poste(models.Model):
    id_poste = models.AutoField(primary_key=True, db_column='id_Poste')
    libelle_poste = models.CharField(max_length=45, db_column='Libelle_Poste')
    class Meta:
        managed = False
        db_table = 'Poste'
    def __str__(self): return self.libelle_poste

class Affectation(models.Model):
    id_employe = models.IntegerField(primary_key=True, db_column='id_Employe')
    id_poste = models.ForeignKey(Poste, on_delete=models.CASCADE, db_column='id_Poste')
    date_debut = models.DateField(db_column='Date_debut')
    date_fin = models.DateField(db_column='Date_fin', null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'Affectation'
        unique_together = [('id_employe', 'id_poste')]
