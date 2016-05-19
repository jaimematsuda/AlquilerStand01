from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from itertools import chain

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)

from .forms import CobranzaForm
from .models import Cobranza
from .models import Contrato 


class CobranzaList(ListView):
	model = Cobranza

	def get_context_data(self, **kwargs):
		context = super(CobranzaList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Cobranza'})
		return context


class CobranzaDetail(DetailView):
	model = Cobranza

	def get_context_data(self, **kwargs):
		context = super(CobranzaDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Cobranza'})
		return context	


class CobranzaCreation(CreateView):
	template_name = 'cobranzas/cobranza_form.html'
	success_url = reverse_lazy('cobranzas:list')
	form_class = CobranzaForm

	def get_context_data(self, **kwargs):
		context = super(CobranzaCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Cobranza'})
		return context


class CobranzaUpdate(UpdateView):
	model = Cobranza
	success_url = reverse_lazy('cobranzas:list')
	fields = ['tipo', 'contrato', 'periodo', 'fecha', 'monto']	

	def get_context_data(self, **kwargs):
		context = super(CobranzaUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Cobranza'})
		return context


class EstadoCuentaList(ListView):
	model = Cobranza  
	template_name = 'cobranzas/estadocuenta_list.html'

	queryset = Cobranza.objects.values('contrato__local__piso', 
									   'contrato__local',
								       'periodo', 'contrato__monto', 
								       'contrato__pk'
								      ).filter(periodo='04-2016'
								      ).annotate(monto_cobrado=Sum('monto'))

	def get_context_data(self, **kwargs):
		context = super(EstadoCuentaList, self).get_context_data(**kwargs)
		contrato_id = Contrato.objects.values_list('pk')
		cobranza_id = Cobranza.objects.values_list('contrato').filter()
		diferencia = list(set(contrato_id) - set(cobranza_id))
		lista_id = []
		for v in diferencia:
			for x in v:
				lista_id.append(x)
		contrato = Contrato.objects.filter(pk__in=lista_id)

		context.update({'titulo': 'Estado de Cuenta'})
		context.update({'contrato': contrato})
		context.update({'diferencia': diferencia})
		context.update({'lista_id': lista_id})

		return context
