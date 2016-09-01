from __future__ import unicode_literals

from django.db import models
#from django.forms import ModelForm

from contratos.models import Contrato


class CobranzaTipo(models.Model):
	nombre = models.CharField(max_length=255, unique=True, blank=True, 
							  null=True)
	class Meta:
		ordering = ('nombre',)

	def __str__(self):
		return self.nombre


class Cobranza(models.Model):
	tipo = models.ForeignKey(CobranzaTipo) ## ALQUILER, MANTENIMIENTO
	contrato = models.ForeignKey(Contrato)
	periodo = models.CharField(max_length=255)
	fecha = models.DateField()
	monto = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		ordering = ('tipo',)
	
	def __str__(self):
		return 	'%s %s %s' % (self.id, self.contrato.local.tipo.nombre, 
			self.contrato.local.numero)









