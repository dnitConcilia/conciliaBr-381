# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20170504_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_item', to='content.Album', verbose_name='Album'),
        ),
    ]