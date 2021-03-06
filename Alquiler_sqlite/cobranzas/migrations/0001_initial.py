# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobranza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.Contrato')),
            ],
            options={
                'ordering': ('tipo',),
            },
        ),
        migrations.CreateModel(
            name='CobranzaTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='cobranza',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cobranzas.CobranzaTipo'),
        ),
    ]
