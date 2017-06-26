# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0004_auto_20170625_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ctrosalud',
            options={'managed': False, 'verbose_name_plural': 'Centros de Salud'},
        ),
        migrations.AlterModelOptions(
            name='estcivil',
            options={'managed': False, 'ordering': ['nom_est_civil'], 'verbose_name_plural': 'Estados Civiles'},
        ),
        migrations.AlterModelOptions(
            name='prevision',
            options={'managed': False, 'verbose_name_plural': 'Previsiones'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'managed': False, 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='salud',
            options={'managed': False, 'verbose_name_plural': 'Salud'},
        ),
        migrations.AlterModelOptions(
            name='tipopaciente',
            options={'managed': False, 'verbose_name_plural': 'Tipos de Pacientes'},
        ),
    ]