from __future__ import unicode_literals

from django.db import models

from gastos.models import Gasto
from mantenimientos.models import Mantenimiento 


class Pago(models.Model):
	fecha = models.DateField()
	
	class Meta:
		ordering = ('fecha',)

	def __str__(self):
		return 	self.fecha


class PagoMantenimiento(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	mantenimiento = models.ForeignKey(Mantenimiento)
	monto = models.DecimalField(max_digits=7, decimal_places=2)


class PagoGasto(models.Model):
	pago = models.OneToOneField(Pago, primary_key=True)
	gasto = models.ForeignKey(Gasto)
	monto = models.DecimalField(max_digits=7, decimal_places=2)




