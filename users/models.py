from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLES = [
        ('admin', 'Administrateur'),
        ('director', 'Directeur'),
        ('head_chef', 'Chef Cuisinier'),
        ('cook', 'Cuisinier'),
        ('server', 'Serveur'),
        ('stock_manager', 'Gestionnaire de Stock'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLES, default='server')
    employe_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} ({self.get_role_display()})'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
