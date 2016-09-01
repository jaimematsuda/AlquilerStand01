from __future__ import unicode_literals

from django.db import models

from lotes.models import Lote
from pagos.models import Pago  


class Caja(models.Model):
	fecha = models.DateField()


class CajaLote(models.Model):
	caja = models.OneToOneField(Caja, primary_key=True)
	lote = models.ForeignKey(Lote)


class CajaPago(models.Model):
	caja = models.OneToOneField(Caja, primary_key=True)
	pago = models.ForeignKey(Pago)
