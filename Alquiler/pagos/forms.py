import datetime
from django import forms

from .models import Pago


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