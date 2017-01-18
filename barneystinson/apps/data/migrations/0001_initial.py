# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='ordre')),
            ],
            options={
                'verbose_name': 'Type de contrat',
                'verbose_name_plural': 'Types de contrat',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='ordre')),
            ],
            options={
                'verbose_name': "Nombre d'employés",
                'verbose_name_plural': "Nombre d'employés",
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='ordre')),
            ],
            options={
                'verbose_name': 'Expérience',
                'verbose_name_plural': 'Expérience',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='ordre')),
            ],
            options={
                'verbose_name': "Secteur d'activité",
                'verbose_name_plural': "Secteurs d'activité",
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='StudyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='ordre')),
            ],
            options={
                'verbose_name': "Niveau d'étude",
                'verbose_name_plural': "Niveaux d'étude",
                'ordering': ['order', 'name'],
            },
        ),
    ]
