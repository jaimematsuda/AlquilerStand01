# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0002_auto_20160601_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimientoperiodo',
            name='mantenimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.Mantenimiento'),
        ),
        migrations.AlterField(
            model_name='mantenimientoperiodo',
            name='periodo',
            field=models.CharField(max_length=255),
        ),
    ]
