from django.contrib import admin

from .models import MantenimientoGrupo, MantenimientoNombre, Mantenimiento


@admin.register(MantenimientoGrupo)
class AdminMantenimientoGrupo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(MantenimientoNombre)
class AdminMantenimientoNombre(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Mantenimiento)
class AdminMantenimiento(admin.ModelAdmin):
	list_display = ('grupo', 'nombre', 'periodo', 'total',)
	list_filter = ('grupo', 'nombre', 'periodo',)
