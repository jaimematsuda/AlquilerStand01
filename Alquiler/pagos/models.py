from __future__ import unicode_literals

from django.db import models

from gastos.models import Gasto
from mantenimientos.models import Mantenimiento 


class PagoTipo(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.nombre


class Pago(models.Model):
	fecha = models.DateField()
	tipo = models.ForeignKey(PagoTipo)
	
	class Meta:
		ordering = ('fecha',)

	def __unicode__(self):
		return u'%s' % (self.fecha)


class PagoMantenimiento(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	mantenimiento = models.ForeignKey(Mantenimiento)
	monto = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return '%s %s' % (self.pago, self.mantenimiento)


class PagoGasto(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	gasto = models.ForeignKey(Gasto)
	monto = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return '%s %s' % (self.pago, self.gasto)


