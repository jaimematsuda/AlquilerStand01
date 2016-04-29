from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Inquilino


class InquilinoList(ListView):
	model = Inquilino

	def get_context_data(self, **kwargs):
		context = super(InquilinoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Inquilinos'})
		return context


class InquilinoDetail(DetailView):
	model = Inquilino

	def get_context_data(self, **kwargs):
		context = super(InquilinoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Inquilino'})
		return context


class InquilinoCreation(CreateView):
	model = Inquilino
	success_url = reverse_lazy('inquilinos:list')
	fields = ['nombre', 'ruc', 'dni', 'telefono', 'direccion'] 

	def get_context_data(self, **kwargs):
		context = super(InquilinoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Inquilino'})
		return context


class InquilinoUpdate(UpdateView):
	model = Inquilino
	success_url = reverse_lazy('inquilinos:list')
	fields = ['nombre', 'ruc', 'dni', 'telefono', 'direccion'] 

	def get_context_data(self, **kwargs):
		context = super(InquilinoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Inquilino'})
		return context


class InquilinoDelete(DeleteView):
	model = Inquilino
	success_url = reverse_lazy('inquilinos:list')

	def get_context_data(self, **kwargs):
		context = super(InquilinoDelete, self).get_context_data(**kwargs)
		context.update({'titulo': 'Borrar Inquilino'})
		return context