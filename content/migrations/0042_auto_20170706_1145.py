# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0041_auto_20170706_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfaq',
            name='slug',
            field=models.SlugField(blank=True, help_text="'slug' é um identificador único que será mostrado na url", max_length=500, null=True, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='slug',
            field=models.SlugField(blank=True, help_text="'slug' é um identificador único que será mostrado na url", max_length=500, null=True, verbose_name='Identificador'),
        ),
    ]
