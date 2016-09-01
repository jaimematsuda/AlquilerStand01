import datetime
from django import forms

from .models import Cobranza, Contrato, CobranzaTipo


class CobranzaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CobranzaForm, self).__init__(*args, **kwargs)
		self.fields['tipo'].queryset = CobranzaTipo.objects.filter(id=1)
		self.fields['contrato'].queryset = Contrato.objects.filter(cobro=1)
		self.fields['fecha'].initial = datetime.date.today()

	class Meta():
		model = Cobranza
		fields = ['tipo', 'contrato', 'periodo', 'fecha', 'monto']
		widgets = {
			'fecha': forms.DateInput(attrs={'id': 'datepicker'}),
		}





