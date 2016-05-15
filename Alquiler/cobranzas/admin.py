from django.contrib import admin

from .models import Cobranza, CobranzaTipo


@admin.register(CobranzaTipo)
class AdminCobranzaTipo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Cobranza)
class AdminCobranza(admin.ModelAdmin):
	list_display = ('tipo', 'contrato', 'periodo', 'fecha', 'monto',)
	list_filter = ('tipo', 'contrato', 'periodo', 'fecha',)


