from __future__ import unicode_literals

from django.db import models


class Inquilino(models.Model):
	nombre = models.CharField(max_length=255, unique=True)
	ruc = models.PositiveIntegerField(blank=True, null=True)
	dni = models.CharField(max_length=255, blank=True, null=True)
	telefono = models.PositiveIntegerField(blank=True, null=True)
	direccion = models.CharField(blank=True, max_length=255, null=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)
