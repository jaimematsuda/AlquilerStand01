import datetime
from django import forms

from .models import Pago, PagoMantenimiento, PagoGasto
from mantenimientos.models import Mantenimiento, MantenimientoPeriodo
from gastos.models import Gasto


class PagoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PagoForm, self).__init__(*args, **kwargs)
		self.fields['fecha'].initial = datetime.date.today()

	class Meta:
		model = Pago
		fields = ['fecha', 'tipo']
		widgets = {
			'fecha': forms.DateInput(attrs={'id': 'datepicker'})
		}


class PagoMantenimientoForm(forms.ModelForm):
	class Meta:
		model = PagoMantenimiento
		exclude = ['pago', 'mantenimiento_periodo']


class PagoGastoForm(forms.ModelForm):
	class Meta:
		model = PagoGasto
		fields = ['pago', 'gasto', 'monto']


PagoMantenimientoFormSet = forms.inlineformset_factory(Pago, PagoMantenimiento, can_delete=False, fields=('pago', 'mantenimiento_periodo', 'monto',))
MantenimientoPeriodoFormSet = forms.inlineformset_factory(Mantenimiento, MantenimientoPeriodo, can_delete=False, fields=('periodo', 'total',))
PagoGastoFormSet = forms.inlineformset_factory(Pago, PagoGasto, can_delete=False, fields=('pago',))