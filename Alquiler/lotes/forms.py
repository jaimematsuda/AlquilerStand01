from django import forms
from django.contrib.admin import widgets

from .models import LoteCobranza, Lote, LotePago
from cobranzas.models import Cobranza, CobranzaTipo
from cobranzas.forms import CobranzaForm
from pagos.forms import PagoForm 


class LoteNuevaCobranzaForm(CobranzaForm):
	def __init__(self, *args, **kwargs):
		super(LoteNuevaCobranzaForm, self).__init__(*args, **kwargs)
		tipo = CobranzaTipo.objects.values('id').filter(nombre='Contrato')
		self.fields['tipo'].initial = tipo[0]['id']


LoteCobranzaFormSet = forms.inlineformset_factory(Cobranza, LoteCobranza, can_delete=False, fields=('lote',))


class LoteEditarCobranzaForm(forms.ModelForm):
	class Meta():
		model = Cobranza
		fields = ['tipo', 'contrato', 'periodo', 'fecha', 'monto']
		widgets = {
			'fecha': forms.DateInput(attrs={'id': 'datepicker'})
		}


class LotePagoForm(forms.ModelForm):
	class Meta():
		model = LotePago
		fields = ['lote', 'pago']