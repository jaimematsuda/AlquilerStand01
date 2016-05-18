from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
)

from .models import Lote


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
	fields = ['id', 'local', 'inquilino', 'inicio', 'vencimiento', 'moneda', 'monto',
			 'vigencia', 'cobro'] 

	def get_context_data(self, **kwargs):
		context = super(LoteUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Lote'})
		return context








