from django import forms
from django.forms import inlineformset_factory
from django.contrib.admin import widgets

from cobranzas.forms import CobranzaForm 
from .models import LoteCobranza, Lote 
from cobranzas.models import Cobranza, CobranzaTipo


class LoteNuevaCobranzaForm(CobranzaForm):
	def __init__(self, *args, **kwargs):
		super(LoteNuevaCobranzaForm, self).__init__(*args, **kwargs)
		tipo = CobranzaTipo.objects.values('id').filter(nombre='Contrato')
		self.fields['tipo'].initial = tipo[0]['id']


LoteCobranzaFormSet = inlineformset_factory(Cobranza, LoteCobranza, can_delete=False, fields=('lote',))


class LoteEditarCobranzaForm(forms.ModelForm):
	class Meta():
		model = Cobranza
		fields = ['tipo', 'contrato', 'periodo', 'fecha', 'monto']
		widgets = {
			'fecha': forms.DateInput(attrs={'id': 'datepicker'})
		}