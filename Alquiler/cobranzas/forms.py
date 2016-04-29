from django import forms

from .models import Cobranza

# Traer de la tabla Contratos los contratos filtrados
# por cobro igual a Debe
class CobranzaForm(forms.ModelForm):
	class Meta:
		model = Cobranza
		queryset = Cobranza.objects.get(contrato_id=1)
		fields = ['contrato', 'periodo', 'fecha_cobranza', 'monto', 'lote']


