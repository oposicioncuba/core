from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.core.models import Member, Location, Address


@receiver(post_save, sender=User)
def create_empty_member(sender, **kwargs):
    if kwargs['created']:
        location = Location.objects.create()
        address = Address.objects.create(location=location)
        Member.objects.create(user=kwargs['instance'], address=address)
