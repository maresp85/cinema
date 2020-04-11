from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    CLIENTE = 'Usuario'
    ASISTENTE = 'Asistente'
    ADMINISTRADOR = 'Administrador'
    ROLE_CHOICES = (
        (CLIENTE, 'Usuario'),
        (ASISTENTE, 'Asistente'),
        (ADMINISTRADOR, 'Administrador'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, max_length=14, null=True, blank=True)

    '''def __str__(self):
        return self.user.username'''

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, role=1)
    instance.profile.save()
