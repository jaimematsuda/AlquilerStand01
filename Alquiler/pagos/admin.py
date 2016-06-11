from django.contrib import admin

from .models import Pago, PagoTipo, PagoGasto, PagoMantenimiento


@admin.register(PagoTipo)
class AdminPagoTipo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Pago)
class AdminPago(admin.ModelAdmin):
	list_display = ('id', 'fecha', 'tipo',)


@admin.register(PagoMantenimiento)
class AdminPagoMantenimiento(admin.ModelAdmin):
	list_display = ('pk', 'pago', 'mantenimiento_periodo', 'monto',)


@admin.register(PagoGasto)
class AdminPagoGasto(admin.ModelAdmin):
	list_display = ('pk', 'pago', 'gasto', 'monto',)
