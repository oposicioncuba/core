# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 13:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171104_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='additional_street',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]