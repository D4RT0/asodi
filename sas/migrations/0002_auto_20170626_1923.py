# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apoderado',
            name='fech_ing_apod',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]