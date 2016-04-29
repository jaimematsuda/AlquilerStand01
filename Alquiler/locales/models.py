from __future__ import unicode_literals

from django.db import models


class LocalTipo(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)


class LocalDivision(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)


class Local(models.Model):
	piso = models.PositiveIntegerField()
	tipo = models.ForeignKey(LocalTipo)
	numero = models.PositiveIntegerField()
	division = models.ForeignKey(LocalDivision, default=1)

	def __str__(self):
		return '%s %s %s %s' % (self.piso, self.tipo, self.numero, self.division)

	class Meta:
		ordering = ('piso', 'tipo', 'numero', 'division',)
		unique_together = (("tipo", "numero", "division"),)


