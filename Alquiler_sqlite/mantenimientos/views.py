from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Mantenimiento


class MantenimientoList(ListView):
	model = Mantenimiento

	def get_context_data(self, **kwargs):
		context = super(MantenimientoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista'})
		return context


class MantenimientoDetail(DetailView):
	model = Mantenimiento

	def get_context_data(self, **kwargs):
		context = super(MantenimientoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class MantenimientoCreation(CreateView):
	model = Mantenimiento
	success_url = reverse_lazy('mantenimientos:list')
	fields = ['id', 'grupo', 'nombre'] 

	def get_context_data(self, **kwargs):
		context = super(MantenimientoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		return context


class MantenimientoUpdate(UpdateView):
	model = Mantenimiento
	success_url = reverse_lazy('mantenimientos:list')
	fields = ['id', 'grupo', 'nombre'] 

	def get_context_data(self, **kwargs):
		context = super(MantenimientoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context






