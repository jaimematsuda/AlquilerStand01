from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Banco


class BancoList(ListView):
	model = Banco

	def get_context_data(self, **kwargs):
		context = super(BancoList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista'})
		return context


class BancoDetail(DetailView):
	model = Banco

	def get_context_data(self, **kwargs):
		context = super(BancoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class BancoCreation(CreateView):
	model = Banco
	success_url = reverse_lazy('bancos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(BancoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		return context


class BancoUpdate(UpdateView):
	model = Banco
	success_url = reverse_lazy('bancos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(BancoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context





