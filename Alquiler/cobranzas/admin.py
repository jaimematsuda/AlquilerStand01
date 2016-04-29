from django.contrib import admin
from .models import Cobranza, CobranzaLote

@admin.register(Cobranza)
class AdminCobranza(admin.ModelAdmin):
	list_display = ('lote', 'contrato', 'periodo', 'fecha_cobranza', 'monto',)
	list_filter = ('lote', 'contrato', 'periodo', 'fecha_cobranza',)

@admin.register(CobranzaLote)
class AdminCobranzaLote(admin.ModelAdmin):
	list_display = ('numero', 'inicio', 'cierre')

