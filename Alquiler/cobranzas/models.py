from __future__ import unicode_literals

from django.db import models
#from django.forms import ModelForm

from contratos.models import Contrato


class CobranzaLote(models.Model):
	numero = models.CharField(max_length=255, unique=True)
	inicio = models.DateField()
	cierre = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.numero


class Cobranza(models.Model):
	contrato = models.ForeignKey(Contrato)
	periodo = models.CharField(max_length=255)
	fecha_cobranza = models.DateField()
	monto = models.DecimalField(max_digits=7, decimal_places=2)
	lote = models.ForeignKey(CobranzaLote)
	
	def __str__(self):
		return 	'%s %s' % (self.contrato.local.tipo.nombre, 
			self.contrato.local.numero)









