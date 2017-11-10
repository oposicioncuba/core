from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Location(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )

    def __str__(self):
        if not self.is_root_node():
            return '%s %s' % (self.name, str(self.parent))
        else:
            return self.name


class Address(TimeStampedModel):
    street = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=10, null=True)
    additional_street = models.TextField(null=True)

    location = models.ForeignKey(Location, null=True)


class Organization(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()

    headquarter = models.ForeignKey(Address)
    leader = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Member(TimeStampedModel):
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    position = models.CharField(max_length=200, null=True)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos', null=True)

    address = models.ForeignKey(Address)
    organization = models.ForeignKey(Organization, null=True)
    user = models.ForeignKey(User, null=True, related_name='member')

from . import signals #  noqa
