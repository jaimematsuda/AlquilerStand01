from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
)

from .models import Lote, LoteCobranza, LotePago
from cobranzas.models import Cobranza
from pagos.models import Pago, PagoMantenimiento, PagoGasto
from cajas.models import Caja, CajaLote
from bancos.models import Banco, BancoLote

from cobranzas.views import CobranzaList


class LoteList(ListView):
	model = Lote

	def get_context_data(self, **kwargs):
		context = super(LoteList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Lote'})
		return context


class LoteDetail(DetailView):
	model = Lote

	def get_context_data(self, **kwargs):
		context = super(LoteDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Lote'})
		return context


class LoteCreation(CreateView):
	model = Lote
	success_url = reverse_lazy('lotes:list')
	fields = ['id', 'numero', 'inicio', 'cierre', 'cobrado', 'gasto', 'total',
			  'revisado'] 

	def get_context_data(self, **kwargs):
		context = super(LoteCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Lote'})
		return context


class LoteUpdate(UpdateView):
	model = Lote
	success_url = reverse_lazy('lotes:list')
	fields = ['id', 'numero', 'inicio', 'cierre', 'cobrado', 'gasto', 'total',
			  'revisado'] 

	def get_context_data(self, **kwargs):
		context = super(LoteUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Lote'})
		return context


class LoteTransaccionContratoList(ListView):
	model = Lote
	context_object_name = 'lote_list'  
	template_name = 'lotes/lotetransaccioncontrato_list.html'

	#queryset = Cobranza.objects.values('contrato__local__piso', 
	#								   'contrato__local',
	#							       'periodo', 'contrato__monto', 
	#							       'contrato__pk'
	#							      ).filter(periodo='04-2016'
	#							      ).annotate(monto_cobrado=Sum('monto'))

	def get_context_data(self, **kwargs):
		context = super(LoteTransaccionContratoList, self).get_context_data(**kwargs)
		lotecobranza = LoteCobranza.objects.values()
		lotepago = LotePago.objects.values()

		context.update({'titulo': 'Estado de Cuenta'})
		context.update({'lotecobranza': lotecobranza})
		context.update({'lotepago': lotepago})

		return context







