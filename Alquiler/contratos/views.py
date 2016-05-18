from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Contrato


class ContratoList(ListView):
	model = Contrato

	def get_context_data(self, **kwargs):
		context = super(ContratoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Contrato'})
		return context


class ContratoDetail(DetailView):
	model = Contrato

	def get_context_data(self, **kwargs):
		context = super(ContratoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Contrato'})
		return context


class ContratoCreation(CreateView):
	model = Contrato
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'local', 'inquilino', 'inicio', 'vencimiento', 'moneda', 'monto',
			  'vigencia', 'cobro'] 

	def get_context_data(self, **kwargs):
		context = super(ContratoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Contrato'})
		return context


class ContratoUpdate(UpdateView):
	model = Contrato
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'local', 'inquilino', 'inicio', 'vencimiento', 'moneda', 'monto',
			 'vigencia', 'cobro'] 

	def get_context_data(self, **kwargs):
		context = super(ContratoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Contrato'})
		return context




