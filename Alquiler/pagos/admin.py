from django.contrib import admin

from .models import Pago, PagoGasto, PagoMantenimiento


@admin.register(Pago)
class AdminPago(admin.ModelAdmin):
	list_display = ('id', 'fecha',)


@admin.register(PagoMantenimiento)
class AdminPagoMantenimiento(admin.ModelAdmin):
	list_display = ('pago', 'mantenimiento', 'monto',)


@admin.register(PagoGasto)
class AdminPagoGasto(admin.ModelAdmin):
	list_display = ('pago', 'gasto', 'monto',)
