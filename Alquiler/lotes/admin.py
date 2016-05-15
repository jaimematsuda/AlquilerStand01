from django.contrib import admin

from .models import Lote, LoteCobranza, LotePago


@admin.register(Lote)
class AdminLote(admin.ModelAdmin):
	list_display = ('numero', 'inicio', 'cierre', 'cobrado', 'gasto', 'total', 'revisado',)


@admin.register(LoteCobranza)
class AdminLoteCobranza(admin.ModelAdmin):
	list_display = ('cobranza', 'lote',)


@admin.register(LotePago)
class AdminLoteCobranza(admin.ModelAdmin):
	list_display = ('pago', 'lote',)
