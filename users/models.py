from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = [
        ('admin',         'Administrateur'),
        ('director',      'Directeur'),
        ('head_chef',     'Chef Cuisinier'),
        ('cook',          'Cuisinier'),
        ('server',        'Serveur'),
        ('stock_manager', 'Gestionnaire de Stock'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='server')
    # Optional: link to your Employe table
    employe_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

