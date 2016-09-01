from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Caja


class CajaList(ListView):
	model = Caja

	def get_context_data(self, **kwargs):
		context = super(CajaList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista Caja'})
		return context


class CajaDetail(DetailView):
	model = Caja

	def get_context_data(self, **kwargs):
		context = super(CajaDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class CajaCreation(CreateView):
	model = Caja
	success_url = reverse_lazy('cajas:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(CajaCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		return context


class CajaUpdate(UpdateView):
	model = Caja
	success_url = reverse_lazy('cajas:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(CajaUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context





