# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobranzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobranza',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranzas.CobranzaTipo'),
        ),
    ]
