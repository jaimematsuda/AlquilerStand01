from django.contrib import admin

from .models import (MantenimientoGrupo, MantenimientoNombre, Mantenimiento, 
					MantenimientoPeriodo)


@admin.register(MantenimientoGrupo)
class AdminMantenimientoGrupo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(MantenimientoNombre)
class AdminMantenimientoNombre(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Mantenimiento)
class AdminMantenimiento(admin.ModelAdmin):
	list_display = ('grupo', 'nombre',)
	list_filter = ('grupo', 'nombre',)


@admin.register(MantenimientoPeriodo)
class AdminMantenimientoPeriodo(admin.ModelAdmin):
	list_display = ('mantenimiento', 'periodo', 'total',)
	list_filter = ('periodo',)
