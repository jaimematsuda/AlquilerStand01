# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0010_auto_20160609_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagomantenimiento',
            name='mantenimiento_periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.MantenimientoPeriodo'),
        ),
    ]
