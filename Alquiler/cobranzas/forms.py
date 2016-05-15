from django import forms

from .models import Cobranza, Contrato

# Traer de la tabla Contratos los contratos filtrados
# por cobro igual a Debe
class CobranzaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CobranzaForm, self).__init__(*args, **kwargs)
		self.fields['contrato'].queryset = Contrato.objects.filter(cobro=1)
	class Meta():
		model = Cobranza
		fields = ['contrato', 'periodo', 'fecha', 'monto']



