from django.contrib import admin

from .models import Banco, BancoLote, BancoPago

@admin.register(Banco)
class AdminBanco(admin.ModelAdmin):
	list_display = ('fecha',)


@admin.register(BancoLote)
class AdminBancoLote(admin.ModelAdmin):
	list_display = ('banco', 'lote', 'monto',)


@admin.register(BancoPago)
class AdminBancoPago(admin.ModelAdmin):
	list_display = ('pago', 'banco',)