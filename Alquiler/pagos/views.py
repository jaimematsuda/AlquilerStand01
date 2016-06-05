import datetime
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Pago, PagoMantenimiento, PagoGasto
from .forms import PagoForm

# Pagos relacionados a MANTENIMIENTO O GASTO
class PagoList(ListView):
	def get_queryset(self):
		month = self.args[0]
		year = self.args[1]
		return Pago.objects.filter(fecha__year=year, fecha__month=month)

	def get_context_data(self, **kwargs):
		context = super(PagoList, self).get_context_data(**kwargs)
		pago_mantenimiento = PagoMantenimiento.objects.all()
		pago_gasto = PagoGasto.objects.all()
		month = self.args[0]
		year = self.args[1]
		context.update({'titulo': 'Lista'})
		context.update({'pago_mantenimiento': pago_mantenimiento})
		context.update({'pago_gasto': pago_gasto})
		context.update({'month': month})
		context.update({'year': year})
		return context


class PagoDetail(DetailView):
	model = Pago

	def get_context_data(self, **kwargs):
		context = super(PagoDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle'})
		return context


class PagoCreation(CreateView):
	template_name = 'pagos/pago_form.html'
	form_class = PagoForm
	success_url = reverse_lazy('pagos:list')

	def get_context_data(self, **kwargs):
		month = self.args[0]
		year = self.args[1]
		context = super(PagoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nueva Transaccion'})
		context.update({'month': month})
		context.update({'year': year})
		return context


class PagoUpdate(UpdateView):
	model = Pago
	success_url = reverse_lazy('pagos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(PagoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context






