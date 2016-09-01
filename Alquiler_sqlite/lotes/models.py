from __future__ import unicode_literals

from django.db import models

from cobranzas.models import Cobranza
from pagos.models import Pago


class Lote(models.Model):
	numero = models.CharField(max_length=255, unique=True)
	inicio = models.DateField()

	class Meta:
		ordering = ('numero',)

	def __str__(self):
		return self.numero


class LoteCierre(models.Model):
	lote = models.OneToOneField(Lote, primary_key=True)
	fecha = models.DateField()
	cobrado = models.DecimalField(max_digits=7, decimal_places=2)
	gasto = models.DecimalField(max_digits=7, decimal_places=2)
	total = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		ordering = ('lote',)

	def __str__(self):
		return u'%s' % (self.fecha)


class LoteRevisado(models.Model):
	lote = models.OneToOneField(Lote, primary_key=True)
	fecha = models.DateField()

	class Meta:
		ordering = ('lote',)

	def __str__(self):
		return u'%s' % (self.fecha)


class LoteCobranza(models.Model):
	cobranza = models.OneToOneField(Cobranza, primary_key=True)
	lote = models.ForeignKey(Lote)


class LotePago(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	lote = models.ForeignKey(Lote)