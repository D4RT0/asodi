# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0008_auto_20170626_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apoderado',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='comuna',
            options={'managed': True, 'ordering': ['com_nom']},
        ),
        migrations.AlterModelOptions(
            name='ctrosalud',
            options={'managed': True, 'verbose_name_plural': 'Centros de Salud'},
        ),
        migrations.AlterModelOptions(
            name='cuota',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'managed': True, 'ordering': ['nom_estado']},
        ),
        migrations.AlterModelOptions(
            name='estcivil',
            options={'managed': True, 'ordering': ['nom_est_civil'], 'verbose_name_plural': 'Estados Civiles'},
        ),
        migrations.AlterModelOptions(
            name='pago',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='patologia',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='prevision',
            options={'managed': True, 'verbose_name_plural': 'Previsiones'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'managed': True, 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='salud',
            options={'managed': True, 'verbose_name_plural': 'Salud'},
        ),
        migrations.AlterModelOptions(
            name='socio',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipopaciente',
            options={'managed': True, 'verbose_name_plural': 'Tipos de Pacientes'},
        ),
        migrations.AlterModelTable(
            name='apoderado',
            table='apoderado',
        ),
        migrations.AlterModelTable(
            name='comuna',
            table='comuna',
        ),
        migrations.AlterModelTable(
            name='ctrosalud',
            table='ctro_salud',
        ),
        migrations.AlterModelTable(
            name='cuota',
            table='cuota',
        ),
        migrations.AlterModelTable(
            name='estado',
            table='estado',
        ),
        migrations.AlterModelTable(
            name='estcivil',
            table='est_civil',
        ),
        migrations.AlterModelTable(
            name='pago',
            table='pago',
        ),
        migrations.AlterModelTable(
            name='patologia',
            table='patologia',
        ),
        migrations.AlterModelTable(
            name='prevision',
            table='prevision',
        ),
        migrations.AlterModelTable(
            name='provincia',
            table='provincia',
        ),
        migrations.AlterModelTable(
            name='region',
            table='region',
        ),
        migrations.AlterModelTable(
            name='salud',
            table='salud',
        ),
        migrations.AlterModelTable(
            name='socio',
            table='socio',
        ),
        migrations.AlterModelTable(
            name='tipopaciente',
            table='tipo_paciente',
        ),
    ]
