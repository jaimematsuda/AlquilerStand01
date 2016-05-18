from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Pago


class PagoList(ListView):
	model = Pago

	def get_context_data(self, **kwargs):
		context = super(PagoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista'})
		return context


class PagoDetail(DetailView):
	model = Pago

	def get_context_data(self, **kwargs):
		context = super(PagoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class PagoCreation(CreateView):
	model = Pago
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(PagoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		return context


class PagoUpdate(UpdateView):
	model = Pago
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(PagoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context






