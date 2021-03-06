# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_auto_20170621_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da categoria')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, null=True, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name_plural': 'Categorias de perguntas frequentes',
                'verbose_name': 'Categoria de perguntas frequentes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Pergunta que será apresentada no site', max_length=500, verbose_name='Pergunta')),
                ('answer', models.CharField(help_text='Resposta para a pergunta que será apresentada no site', max_length=500, verbose_name='Resposta')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.CategoryFaq', verbose_name='Categoria')),
            ],
            options={
                'verbose_name_plural': 'Perguntas Frequentes',
                'verbose_name': 'Pergunta Frequente',
                'ordering': ['question'],
            },
        ),
    ]
