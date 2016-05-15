from django.contrib import admin


from .models import Caja, CajaLote, CajaPago


@admin.register(Caja)
class AdminCaja(admin.ModelAdmin):
	list_display = ('fecha',)


@admin.register(CajaLote)
class AdminCajaLote(admin.ModelAdmin):
	list_diplay = ('cobranza', 'caja', 'monto',)


@admin.register(CajaPago)
class AdminCajaPago(admin.ModelAdmin):
	list_diplay = ('caja', 'pago',)
	