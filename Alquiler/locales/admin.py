from django.contrib import admin
from .models import Local, LocalTipo, LocalDivision


@admin.register(LocalTipo)
class AdminLocalTipo(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(LocalDivision)
class AdminLocalDivision(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Local)
class AdminLocal(admin.ModelAdmin):
	list_display = ('piso', 'tipo', 'numero', 'division',)
	list_filter = ('piso', 'tipo',)

