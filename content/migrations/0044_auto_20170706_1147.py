# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0043_auto_20170706_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryfaq',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='slug',
        ),
    ]
