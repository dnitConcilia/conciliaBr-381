# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0047_atareuniao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atareuniao',
            name='date_ata_reuniao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da Ata de reunião'),
        ),
    ]