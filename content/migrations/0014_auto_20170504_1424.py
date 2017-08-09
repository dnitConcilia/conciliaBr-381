# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20170504_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunidade',
            name='num_latitude',
        ),
        migrations.RemoveField(
            model_name='comunidade',
            name='num_longitude',
        ),
        migrations.AddField(
            model_name='comunidade',
            name='lat_long',
            field=models.CharField(blank=True, max_length=500, verbose_name='Informe as coordenadas: Latitude e Longitude obtidas através do googleMaps'),
        ),
    ]