from __future__ import unicode_literals

from django.db import models

from lotes.models import Lote
from pagos.models import Pago  


class Banco(models.Model):
	fecha = models.DateField()


class BancoLote(models.Model):
	banco = models.OneToOneField(Banco, primary_key=True)
	lote = models.ForeignKey(Lote)
	monto = models.DecimalField(max_digits=7, decimal_places=2)


class BancoPago(models.Model):
	banco = models.OneToOneField(Banco, primary_key=True)
	pago = models.ForeignKey(Pago)



	