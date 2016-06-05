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

	class Meta:
		ordering = ('grupo', 'nombre',)
		unique_together =('grupo', 'nombre')

	def __str__(self):
		return '%s %s' % (self.grupo, self.nombre)


class MantenimientoPeriodo(models.Model):
	mantenimiento = models.ForeignKey(Mantenimiento)
	periodo = models.CharField(max_length=255)
	total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

	class Meta:
		ordering =('periodo',)
		unique_together = ('mantenimiento', 'periodo')

	def __str__(self):
		return '%s %s' % (self.mantenimiento, self.periodo)