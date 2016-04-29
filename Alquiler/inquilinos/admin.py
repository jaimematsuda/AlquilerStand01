from django.contrib import admin
from .models import Inquilino


@admin.register(Inquilino)
class AdminLocalTipo(admin.ModelAdmin):
	list_display = ('nombre', 'ruc', 'dni', 'telefono', 'direccion')
	

