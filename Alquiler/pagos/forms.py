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


class MantenimientoPeriodoForm(forms.ModelForm):
	class Meta:
		model = MantenimientoPeriodo
		fields = ['mantenimiento', 'periodo']


class MantenimientoForm(forms.ModelForm):
	class Meta:
		model = Mantenimiento
		fields = ['grupo', 'nombre']		


PagoMantenimientoFormSet = forms.inlineformset_factory(Pago, PagoMantenimiento, can_delete=False, fields=('pago', 'mantenimiento_periodo', 'monto',))
MantenimientoPeriodoFormSet = forms.inlineformset_factory(Mantenimiento, MantenimientoPeriodo, can_delete=False, fields=('periodo', 'total',))
PagoGastoFormSet = forms.inlineformset_factory(Pago, PagoGasto, can_delete=False, fields=('pago',))