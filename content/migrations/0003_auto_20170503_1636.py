# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170503_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='legend_image',
            field=models.CharField(max_length=200, null=True, verbose_name='Legenda da imagem'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='sub_title',
            field=models.CharField(max_length=200, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
