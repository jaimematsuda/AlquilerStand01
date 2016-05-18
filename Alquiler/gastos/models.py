from __future__ import unicode_literals

from django.db import models


class GastoGrupo(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.nombre


class GastoNombre(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('nombre',)

	def __str__(self):
		return self.nombre


class Gasto(models.Model):
	grupo = models.ForeignKey(GastoGrupo)
	nombre = models.ForeignKey(GastoNombre)
	total = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		ordering =('nombre',)

	def __str__(self):
		return '%s %s' % (self.grupo, self.nombre)
