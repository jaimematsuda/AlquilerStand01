# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0005_auto_20160601_1605'),
        ('pagos', '0009_auto_20160601_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagomantenimiento',
            name='mantenimiento',
        ),
        migrations.AddField(
            model_name='pagomantenimiento',
            name='mantenimiento_periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.MantenimientoPeriodo'),
        ),
    ]
