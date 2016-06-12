import datetime
from django.http import HttpResponseRedirect
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
from .forms import PagoForm, PagoMantenimientoForm, PagoGastoForm
from mantenimientos.models import MantenimientoPeriodo
from mantenimientos.forms import MantenimientoForm, MantenimientoPeriodoForm

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
	success_url = reverse_lazy('pagos:list month year')
	form_class = PagoForm

	def get_context_data(self, **kwargs):
		month = self.args[0]
		year = self.args[1]
		context = super(PagoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Pago'})
		context.update({'month': month})
		context.update({'year': year})
		return context

	def get(self, request, *args, **kwargs):
		"""
		Handles GET requests and instantiates blank versions of the form
		and its inline formsets.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		# prueba post pagomantenimiento_form = PagoMantenimientoForm()
		# prueba post mantenimientoperiodo_form = MantenimientoPeriodoForm()
		return self.render_to_response(self.get_context_data(form=form, 
			#pagomantenimiento_form=pagomantenimiento_form,
			#mantenimientoperiodo_form=mantenimientoperiodo_form,
			))

	'''	
	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		mantenimientoperiodo_form = MantenimientoPeriodoForm(self.request.POST)
		pagomantenimiento_form = PagoMantenimientoForm(self.request.POST)
		if (form.is_valid() and mantenimientoperiodo_form.is_valid()):
		    return self.form_valid(form, mantenimientoperiodo_form, 
		    	pagomantenimiento_form)
		else:
		    return self.form_invalid(form, mantenimientoperiodo_form, 
		    	pagomantenimiento_form)
	'''
	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		paso = self.request.POST.get('monto')
		tipo = self.request.POST.get('tipo')
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		if not paso:
			mantenimientoperiodo_form = MantenimientoPeriodoForm()
			pagomantenimiento_form = PagoMantenimientoForm()
			pagogasto_form = PagoGastoForm()

			if (tipo == '1'):
				return self.render_to_response(self.get_context_data(form=form, 
					mantenimientoperiodo_form=mantenimientoperiodo_form,
					pagomantenimiento_form=pagomantenimiento_form,
					))

			if (tipo == '2'):
				return self.render_to_response(self.get_context_data(form=form, 
					pagogasto_form=pagogasto_form,
					))

		if (tipo == '1'):
			mantenimientoperiodo_form = MantenimientoPeriodoForm(self.request.POST)
			pagomantenimiento_form = PagoMantenimientoForm(self.request.POST)
			
			if (form.is_valid() and mantenimientoperiodo_form.is_valid()):
			    return self.form_valid(form, mantenimientoperiodo_form, 
			    	pagomantenimiento_form)
			else:
			    return self.form_invalid(form, mantenimientoperiodo_form, 
			    	pagomantenimiento_form)
		
	def form_valid(self, form, mantenimientoperiodo_form, 
		pagomantenimiento_form):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		self.object = form.save()
		mantenimientoperiodo_form.save()
		id_mantperi = MantenimientoPeriodo.objects.order_by('id').last()
		id_pago = Pago.objects.order_by('id').last()
		nuevo_pagomantenimiento = pagomantenimiento_form.save(commit=False)
		nuevo_pagomantenimiento.pago = id_pago
		nuevo_pagomantenimiento.mantenimiento_periodo = id_mantperi
		nuevo_pagomantenimiento.save()
		return HttpResponseRedirect(self.get_success_url())

	'''
	article = Article.object.get(pk=1)    # se obtiene el objeto
	pagomantenimiento_form = PagoMantenimientoForm(instance=article) # carga los datos del la base al form

	'''

	def form_invalid(self, form, mantenimientoperiodo_form, 
		pagomantenimiento_form):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		return self.render_to_response(self.get_context_data(form=form, 
			mantenimientoperiodo_form=mantenimientoperiodo_form,
			pagomantenimiento_form=pagomantenimiento_form,
			))

	'''	
	self.object = None
	form_class = self.get_form_class()
	form = self.get_form(form_class)
	mantenimientoperiodo_form = MantenimientoPeriodoForm(self.request.POST)
	pagomantenimiento_form = PagoMantenimientoForm(self.request.POST)
	if (form.is_valid() and mantenimientoperiodo_form.is_valid()):
	    return self.form_valid(form, mantenimientoperiodo_form, 
	    	pagomantenimiento_form)
	else:
	    return self.form_invalid(form, mantenimientoperiodo_form, 
	    	pagomantenimiento_form)
	'''


class PagoUpdate(UpdateView):
	model = Pago
	success_url = reverse_lazy('pagos:list')
	fields = ['id', 'fecha'] 

	def get_context_data(self, **kwargs):
		context = super(PagoUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Transaccion'})
		return context






