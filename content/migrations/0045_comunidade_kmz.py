# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0044_auto_20170706_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidade',
            name='kmz',
            field=models.FileField(blank=True, upload_to='Comunidades/KMZ/', verbose_name='kMZ'),
        ),
    ]