# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20170504_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='legend_image',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Legenda da imagem'),
        ),
    ]