from django.contrib import admin
from .models import Contrato, Moneda, Cobro, Vigencia


@admin.register(Moneda)
class AdminMoneda(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Cobro)
class AdminCobro(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Vigencia)
class AdminVigencia(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Contrato)
class AdminContrato(admin.ModelAdmin):
	list_display = ('id', 'local', 'inquilino', 'inicio', 'vencimiento', 'moneda', 
					'monto', 'vigencia', 'cobro',)
	list_filter = ('local', 'inquilino', 'vigencia', 'cobro',)