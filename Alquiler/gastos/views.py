from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Gasto


class GastoList(ListView):
	model = Gasto

	def get_context_data(self, **kwargs):
		context = super(GastoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista'})
		return context


class GastoDetail(DetailView):
	model = Gasto

	def get_context_data(self, **kwargs):
		context = super(GastoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class GastoCreation(CreateView):
	model = Gasto
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(GastoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		return context


class GastoUpdate(UpdateView):
	model = Gasto
	success_url = reverse_lazy('contratos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(GastoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context






