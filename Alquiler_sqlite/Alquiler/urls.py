from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
#from django.conf.urls.statics import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^banco/' , include('bancos.urls', namespace='bancos')),
    url(r'^caja/' , include('cajas.urls', namespace='cajas')),
    url(r'^cobranza/', include('cobranzas.urls', namespace='cobranzas')),
    url(r'^contrato/' , include('contratos.urls', namespace='contratos')),
    url(r'^gasto/' , include('gastos.urls', namespace='gastos')),
    url(r'^inquilino/' , include('inquilinos.urls', namespace='inquilinos')),
    url(r'^local/' , include('locales.urls', namespace='locales')),
    url(r'^lote/' , include('lotes.urls', namespace='lotes')),
    url(r'^mantenimiento/' , include('mantenimientos.urls', namespace='mantenimientos')),
    url(r'^pago/' , include('pagos.urls', namespace='pagos')),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
