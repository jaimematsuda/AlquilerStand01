from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Local, LocalTipo, Local


class LocalList(ListView):
	model = Local 

	def get_context_data(self, **kwargs):
		context = super(LocalList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Locales'})
		return context


class LocalDetail(DetailView):
	model = Local

	def get_context_data(self, **kwargs):
		context = super(LocalDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Local'})
		return context


class LocalCreation(CreateView):
	model = Local
	success_url = reverse_lazy('locales:list')
	fields = ['piso', 'tipo', 'numero', 'division'] 

	def get_context_data(self, **kwargs):
		context = super(LocalCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Local'})
		return context


class LocalUpdate(UpdateView):
	model = Local
	success_url = reverse_lazy('locales:list')
	fields = ['piso', 'tipo', 'numero', 'division'] 

	def get_context_data(self, **kwargs):
		context = super(LocalUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Local'})
		return context


class LocalDelete(DeleteView):
	model = Local
	success_url = reverse_lazy('locales:list')

	def get_context_data(self, **kwargs):
		context = super(LocalDelete, self).get_context_data(**kwargs)
		context.update({'titulo': 'Borrar Local'})
		return context