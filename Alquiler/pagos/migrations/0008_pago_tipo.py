# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0007_auto_20160601_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagos.PagoTipo'),
        ),
    ]
