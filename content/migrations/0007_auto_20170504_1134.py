# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0006_noticia_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Título do album')),
                ('slug', models.SlugField()),
                ('summary', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Albuns',
                'verbose_name': 'Album',
            },
        ),
        migrations.CreateModel(
            name='Comunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Nome da Vila ou Comunidade')),
                ('about', tinymce.models.HTMLField(verbose_name='Sobre')),
                ('num_latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('num_longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Comunidades/Vilas',
                'verbose_name': 'Comunidade/Vila',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Título')),
                ('legend', models.TextField(blank=True, null=True, verbose_name='Legenda')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='fotos/%Y/%m')),
                ('is_cover_photo', models.BooleanField()),
                ('photographer', models.CharField(max_length=200, verbose_name='Nome do Fotografo')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Album')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Fotos',
                'verbose_name': 'Foto',
            },
        ),
        migrations.AlterField(
            model_name='noticia',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='expired_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de expiração da notícia'),
        ),
        migrations.AddField(
            model_name='comunidade',
            name='photos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Photo'),
        ),
    ]
