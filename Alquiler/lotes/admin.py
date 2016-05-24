from django.contrib import admin

from .models import Lote, LoteCierre, LoteRevisado, LoteCobranza, LotePago


@admin.register(Lote)
class AdminLote(admin.ModelAdmin):
	list_display = ('numero', 'inicio',)


@admin.register(LoteCierre)
class AdminLoteCierre(admin.ModelAdmin):
	list_display = ('lote', 'fecha', 'cobrado', 'gasto', 'total',)


@admin.register(LoteRevisado)
class AdminLoteRevisado(admin.ModelAdmin):
	list_display = ('lote', 'fecha',)


@admin.register(LoteCobranza)
class AdminLoteCobranza(admin.ModelAdmin):
	list_display = ('cobranza', 'lote',)


@admin.register(LotePago)
class AdminLoteCobranza(admin.ModelAdmin):
	list_display = ('pago', 'lote',)
