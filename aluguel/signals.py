from .models import Cliente
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver


@receiver(post_save, sender=User)
def usuario_cliente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(nome=instance.username, user=instance)

post_save.connect(usuario_cliente,sender=User)