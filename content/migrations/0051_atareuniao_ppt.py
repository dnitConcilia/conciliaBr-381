# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0050_auto_20170711_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='atareuniao',
            name='ppt',
            field=models.FileField(default=None, upload_to='apresentacao_reuniao/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
