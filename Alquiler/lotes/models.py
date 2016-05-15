from __future__ import unicode_literals

from django.db import models

from cobranzas.models import Cobranza
from pagos.models import Pago


class Lote(models.Model):
	numero = models.CharField(max_length=255, unique=True)
	inicio = models.DateField()
	cierre = models.DateField(blank=True, null=True)
	cobrado = models.DecimalField(max_digits=7, decimal_places=2, blank=True,
							   null=True)
	gasto = models.DecimalField(max_digits=7, decimal_places=2, blank=True,
								null=True)
	total = models.DecimalField(max_digits=7, decimal_places=2, blank=True,
								null=True)
	revisado = models.DateField(blank=True, null=True)

	class Meta:
		ordering = ('numero',)

	def __str__(self):
		return self.numero


class LoteCobranza(models.Model):
	cobranza = models.OneToOneField(Cobranza, primary_key=True)
	lote = models.ForeignKey(Lote)


class LotePago(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	lote = models.ForeignKey(Lote)