import datetime
from django import forms
from django.forms import extras
from django.contrib.admin.widgets import AdminDateWidget

from .models import Cobranza, Contrato

# Traer de la tabla Contratos los contratos filtrados
# por cobro igual a Debe
class CobranzaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CobranzaForm, self).__init__(*args, **kwargs)
		self.fields['contrato'].queryset = Contrato.objects.filter(cobro=1)
		self.fields['fecha'].initial = datetime.date.today()

	class Meta():
		model = Cobranza
		fields = ['tipo', 'contrato', 'periodo', 'fecha', 'monto']
		#widgets = {'fecha': extras.SelectDateWidget()}




