from django import forms

from .models import Mantenimiento, MantenimientoPeriodo


class MantenimientoPeriodoForm(forms.ModelForm):
	class Meta:
		model = MantenimientoPeriodo
		fields = ['mantenimiento', 'periodo']


class MantenimientoForm(forms.ModelForm):
	class Meta:
		model = Mantenimiento
		fields = ['grupo', 'nombre']