from __future__ import unicode_literals

from django.db import models


class MantenimientoGrupo(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.nombre


class MantenimientoNombre(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('nombre',)

	def __str__(self):
		return self.nombre


class Mantenimiento(models.Model):
	grupo = models.ForeignKey(MantenimientoGrupo)
	nombre = models.ForeignKey(MantenimientoNombre)
	periodo = models.CharField(max_length=255)
	monto = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		ordering =('periodo', 'grupo', 'nombre',)