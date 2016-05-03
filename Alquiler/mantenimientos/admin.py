from django.contrib import admin

from .models import MantenimientoGrupo, MantenimientoNombre, Mantenimiento

# Register your models here.
@admin.register(MantenimientoGrupo)
class AdminMantenimientoGrupo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(MantenimientoNombre)
class AdminMantenimientoNombre(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Mantenimiento)
class AdminMantenimiento(admin.ModelAdmin):
	list_display = ('grupo', 'nombre', 'periodo', 'monto',)
	list_filter = ('grupo', 'nombre', 'periodo',)
