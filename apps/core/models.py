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


class Address(TimeStampedModel):
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    additional_street = models.TextField()

    location = models.ForeignKey(Location)


class Organization(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()

    headquarter = models.ForeignKey(Address)
    leader = models.ForeignKey(User)


class Member(TimeStampedModel):
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    birthday = models.DateTimeField(null=True)
    position = models.CharField(max_length=200, null=True)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos', null=True)

    address = models.ForeignKey(Address)
    organization = models.ForeignKey(Organization, null=True)
    user = models.ForeignKey(User, null=True)
