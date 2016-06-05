from __future__ import unicode_literals

from django.db import models
from locales.models import Local
from inquilinos.models import Inquilino


class Moneda(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre


class Cobro(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.nombre


class Vigencia(models.Model):
	nombre = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.nombre


class Contrato(models.Model):
	# el numero del contrato es el pk
	local = models.ForeignKey(Local)
	inquilino = models.ForeignKey(Inquilino)
	inicio = models.DateField()
	vencimiento = models.DateField()
	moneda = models.ForeignKey(Moneda)
	monto = models.DecimalField(max_digits=7, decimal_places=2)
	vigencia = models.ForeignKey(Vigencia, default=1)
	cobro = models.ForeignKey(Cobro, default=1)

	class Meta:
		ordering = ('local', 'inquilino', 'vencimiento')
		unique_together = ('local' , 'inquilino', 'inicio')	
	
	def __str__(self):
		return '%s %s %s %s' % (self.id, self.local.tipo.nombre, 
							 self.local.numero, self.local.division)


	# 
	# Validado por numero no se repite
	# Validado por la clave local, inquilino, inicio, estos 3 juntos no se debe
	# repetir
	#
		
		