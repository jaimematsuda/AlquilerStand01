from django.db.models import Sum
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
)

from .models import Lote, LoteCobranza, LotePago
from cobranzas.models import Cobranza
from pagos.models import Pago, PagoMantenimiento, PagoGasto
from cajas.models import Caja, CajaLote
from bancos.models import Banco, BancoLote

from cobranzas.views import CobranzaList
from pagos.views import PagoCreation

from .forms import (LoteNuevaCobranzaForm, LoteCobranzaFormSet, 
	LoteEditarCobranzaForm, LotePagoForm)
from pagos.forms import PagoForm, PagoMantenimientoForm, PagoGastoForm
from mantenimientos.forms import MantenimientoForm, MantenimientoPeriodoForm


class LoteList(ListView):
	model = Lote

	def get_context_data(self, **kwargs):
		context = super(LoteList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista de Lote'})
		return context


class LoteDetail(DetailView):
	model = Lote

	def get_context_data(self, **kwargs):
		context = super(LoteDetail, self).get_context_data(**kwargs)
		context.update({'titulo': 'Detalle de Lote'})
		return context


class LoteCreation(CreateView):
	model = Lote
	success_url = reverse_lazy('lotes:list')
	fields = ['id', 'numero', 'inicio', 'cierre', 'cobrado', 'gasto', 'total',
			  'revisado'] 

	def get_context_data(self, **kwargs):
		context = super(LoteCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Lote'})
		return context


class LoteUpdate(UpdateView):
	model = Lote
	success_url = reverse_lazy('lotes:list')
	fields = ['id', 'numero', 'inicio']

	def get_context_data(self, **kwargs):
		context = super(LoteUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Lote'})
		return context


class LoteCobranzaList(ListView):
	model = LoteCobranza 

	def get_context_data(self, **kwargs):
		context = super(LoteCobranzaList, self).get_context_data(**kwargs)
		context.update({'titulo': 'Lista Lote de Cobranzas'})
		return context


class LoteCobranzaCreation(CreateView):
	model = LoteCobranza
	success_url = reverse_lazy('lotes:list_lotecobranza')
	fields = ['cobranza', 'lote'] 

	def get_context_data(self, **kwargs):
		context = super(LoteCobranzaCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Lote de Cobranza'})
		return context


class LoteCobranzaUpdate(UpdateView):
	model = LoteCobranza 
	success_url = reverse_lazy('lotes:list_lotecobranza')
	fields = ['cobranza', 'lote']

	def get_context_data(self, **kwargs):
		context = super(LoteCobranzaUpdate, self).get_context_data(**kwargs)
		context.update({'titulo': 'Editar Lote de Cobranza'})
		return context


class LoteTransaccionContratoList(ListView):
	#model = Lote
	context_object_name = 'ultimo_lote'  
	template_name = 'lotes/lotetransaccioncontrato_list.html'
	#queryset = Lote.objects.order_by('id').last()

	def get_queryset(self):
		if self.args == ():
			return Lote.objects.order_by('id').last()
		else:
			num = '%s-%s' % (self.args[0], self.args[1])
			return Lote.objects.get(numero=num)

	def get_context_data(self, **kwargs):
		context = super(LoteTransaccionContratoList, self).get_context_data(
			**kwargs)
		lote_cobranza = LoteCobranza.objects.filter(
			lote=context['ultimo_lote'], cobranza__tipo__id=1)
		cobranza_total = LoteCobranza.objects.filter(
			lote=context['ultimo_lote'], cobranza__tipo__id=1).aggregate(
			total=Sum('cobranza__monto'))
		lote_pago = LotePago.objects.filter(
			lote=context['ultimo_lote'])
		pago_mantenimiento = PagoMantenimiento.objects.all()
		pago_gasto = PagoGasto.objects.all()
		rango_med = context['ultimo_lote']
		rango_inicio = rango_med.id - 20
		ultimo = Lote.objects.order_by('id').last()
		rango_final = ultimo.id
		lote_lista = Lote.objects.filter(id__range=[rango_inicio, rango_final])

		context.update({'titulo': 'Transacciones'})
		context.update({'lote_cobranza': lote_cobranza})
		context.update({'cobranza_total': cobranza_total})
		context.update({'lote_pago': lote_pago})
		context.update({'pago_mantenimiento': pago_mantenimiento})
		context.update({'pago_gasto': pago_gasto})
		context.update({'lote_lista': lote_lista})
		return context

class LoteNuevaCobranzaCreation(CreateView):
	template_name = 'lotes/lotenuevacobranza_form.html'
	success_url = reverse_lazy('lotes:transaction')
	form_class = LoteNuevaCobranzaForm
	
	def get(self, request, *args, **kwargs):
		"""
		Handles GET requests and instantiates blank versions of the form
		and its inline formsets.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		ultimo_lote_id = Lote.objects.order_by('id').last()
		lotecobranza_form = LoteCobranzaFormSet(initial=[{'lote': ultimo_lote_id}])
		return self.render_to_response(self.get_context_data(form=form, lotecobranza_form=lotecobranza_form))

	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		lotecobranza_form = LoteCobranzaFormSet(self.request.POST)
		if (form.is_valid() and lotecobranza_form.is_valid()):
		    return self.form_valid(form, lotecobranza_form)
		else:
		    return self.form_invalid(form, lotecobranza_form)

	def form_valid(self, form, lotecobranza_form):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		self.object = form.save()
		lotecobranza_form.instance = self.object
		lotecobranza_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, lotecobranza_form):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		return self.render_to_response(
		self.get_context_data(form=form,
		                      lotecobranza_form=lotecobranza_form))
		

class LoteNuevaCobranzaUpdate(UpdateView):
	model = Cobranza 
	template_name = 'lotes/loteeditarcobranza_form.html'
	success_url = reverse_lazy('lotes:transaction')
	form_class = LoteEditarCobranzaForm

	def get(self, request, *args, **kwargs):
		"""
		Handles GET requests and instantiates blank versions of the form
		and its inline formsets.
		"""
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		ultimo_lote_id = Lote.objects.order_by('id').last()
		lotecobranza_form = LoteCobranzaFormSet(initial=[{'lote': ultimo_lote_id}])
		return self.render_to_response(self.get_context_data(form=form, lotecobranza_form=lotecobranza_form))

	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		lotecobranza_form = LoteCobranzaFormSet(self.request.POST)
		if (form.is_valid() and lotecobranza_form.is_valid()):
		    return self.form_valid(form, lotecobranza_form)
		else:
		    return self.form_invalid(form, lotecobranza_form)

	def form_valid(self, form, lotecobranza_form):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		self.object = form.save()
		lotecobranza_form.instance = self.object
		lotecobranza_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, lotecobranza_form):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		return self.render_to_response(
		self.get_context_data(form=form,
		                      lotecobranza_form=lotecobranza_form))

class LoteNuevoPagoCreation(CreateView):
	template_name = 'lotes/lotenuevopago_form.html'
	success_url = reverse_lazy('lotes:transaction')
	form_class = PagoForm

	def get_context_data(self, *args, **kwargs):
		context = super(LoteNuevoPagoCreation, self).get_context_data(**kwargs)
		context.update({'titulo': 'Nuevo Pago Lote'})
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


	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = None
		tipopago = self.request.POST.get('monto')
		tipo = self.request.POST.get('tipo')
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		if not tipopago:
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
				kwargs['mantenimientoperiodo_form'] = mantenimientoperiodo_form
				kwargs['pagomantenimiento_form'] = pagomantenimiento_form
				return self.form_valid(form, tipo, **kwargs)
			else:
			    #return self.form_invalid(form, mantenimientoperiodo_form, pagomantenimiento_form, tipo)
				kwargs['mantenimientoperiodo_form'] = mantenimientoperiodo_form
				kwargs['pagomantenimiento_form'] = pagomantenimiento_form
				return self.form_invalid(form, tipo, **kwargs)

		if (tipo == '2'):
			pagogasto_form = PagoGastoForm(self.request.POST)
			
			if (form.is_valid() and pagogasto_form.is_valid()):
				kwargs['pagogasto_form'] = pagogasto_form
				return self.form_valid(form, tipo, **kwargs)
			else:
				kwargs['pagogasto_form'] = pagogasto_form
				return self.form_invalid(form, tipo, **kwargs)

	
	#def form_valid(self, form, mantenimientoperiodo_form, 
	#	pagomantenimiento_form, tipo):
	def form_valid(self, form, tipo, **kwargs):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		if tipo == '1':
			self.object = form.save()
			mantenimientoperiodo_form = kwargs['mantenimientoperiodo_form']
			pagomantenimiento_form = kwargs['pagomantenimiento_form']
			mantenimientoperiodo_form.save()
			id_mantperi = MantenimientoPeriodo.objects.order_by('id').last()
			id_pago = Pago.objects.order_by('id').last()
			nuevo_pagomantenimiento = pagomantenimiento_form.save(commit=False)
			nuevo_pagomantenimiento.pago = id_pago
			nuevo_pagomantenimiento.mantenimiento_periodo = id_mantperi
			nuevo_pagomantenimiento.save()
			lotepago_form = LotePagoForm()
			ultimo_lote_id = Lote.objects.order_by('id').last()
			nuevo_lotepago = lotepago_form.save(commit=False)
			nuevo_lotepago.pago = id_pago
			nuevo_lotepago.lote = ultimo_lote_id
			nuevo_lotepago.save()
			return HttpResponseRedirect(self.get_success_url())

		if tipo == '2':
			self.object = form.save()
			pagogasto_form = kwargs['pagogasto_form']
			id_pago = Pago.objects.order_by('id').last()
			nuevo_pagogasto = pagogasto_form.save(commit=False)
			nuevo_pagogasto.pago = id_pago
			nuevo_pagogasto.save()
			lotepago_form = LotePagoForm()
			ultimo_lote_id = Lote.objects.order_by('id').last()
			nuevo_lotepago = lotepago_form.save(commit=False)
			nuevo_lotepago.pago = id_pago
			nuevo_lotepago.lote = ultimo_lote_id
			nuevo_lotepago.save()
			return HttpResponseRedirect(self.get_success_url())			

	def form_invalid(self, form, tipo, **kwargs):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		if tipo == '1':
			mantenimientoperiodo_form = kwargs['mantenimientoperiodo_form']
			pagomantenimiento_form = kwargs['pagomantenimiento_form']
			return self.render_to_response(self.get_context_data(form=form, 
				mantenimientoperiodo_form=mantenimientoperiodo_form,
				pagomantenimiento_form=pagomantenimiento_form,
				))

		if tipo == '2':
			pagogasto_form = kwargs['pagogasto_form']
			return self.render_to_response(self.get_context_data(form=form, 
				pagogasto_form=pagogasto_form,
				))






"""
class LoteNuevoPagoCreation(PagoCreation):
	def __init__(self, *args, **kwargs):
		super(LoteNuevoPagoCreation, self).__init__(*args, **kwargs)
		self.success_url = reverse_lazy('lotes:transaction')

		PagoCreation.__init__.form_valid(self, form, tipo, **kwargs)

		#def form_valid(self, form, tipo, **kwargs):
"""
"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
"""
"""
		if tipo == '1':
			lotepago_form = LotePagoForm()
			ultimo_lote_id = Lote.objects.order_by('id').last()
			id_pago = Pago.objects.order_by('id').last()
			nuevo_lotepago = lotepago_form.save(commit=False)
			nuevo_lotepago.pago = id_pago
			nuevo_lotepago.lote = ultimo_lote_id
			nuevo_lotepago.save()
			return HttpResponseRedirect(self.get_success_url())

		if tipo == '2':
			lotepago_form = LotePagoForm()
			ultimo_lote_id = Lote.objects.order_by('id').last()
			id_pago = Pago.objects.order_by('id').last()
			nuevo_lotepago = lotepago_form.save(commit=False)
			nuevo_lotepago.pago = id_pago
			nuevo_lotepago.lote = ultimo_lote_id
			nuevo_lotepago.save()
			return HttpResponseRedirect(self.get_success_url())

		'''
		if tipo == '1':
			self.object = form.save()
			mantenimientoperiodo_form = kwargs['mantenimientoperiodo_form']
			pagomantenimiento_form = kwargs['pagomantenimiento_form']
			mantenimientoperiodo_form.save()
			id_mantperi = MantenimientoPeriodo.objects.order_by('id').last()
			id_pago = Pago.objects.order_by('id').last()
			nuevo_pagomantenimiento = pagomantenimiento_form.save(commit=False)
			nuevo_pagomantenimiento.pago = id_pago
			nuevo_pagomantenimiento.mantenimiento_periodo = id_mantperi
			nuevo_pagomantenimiento.save()
			return HttpResponseRedirect(self.get_success_url())

		if tipo == '2':
			self.object = form.save()
			pagogasto_form = kwargs['pagogasto_form']
			id_pago = Pago.objects.order_by('id').last()
			nuevo_pagogasto = pagogasto_form.save(commit=False)
			nuevo_pagogasto.pago = id_pago
			nuevo_pagogasto.save()
			return HttpResponseRedirect(self.get_success_url())	
		'''
"""