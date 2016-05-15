from django.contrib import admin

from .models import Gasto, GastoGrupo, GastoNombre


@admin.register(GastoGrupo)
class AdminGastoGrupo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(GastoNombre)
class AdminGastoNombre(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Gasto)
class AdminGasto(admin.ModelAdmin):
	list_display = ('grupo', 'nombre', 'total',)


