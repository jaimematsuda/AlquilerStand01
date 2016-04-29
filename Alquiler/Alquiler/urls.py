from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
#from django.conf.urls.statics import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^local/' , include('locales.urls', namespace='locales')),
    url(r'^inquilino/' , include('inquilinos.urls', namespace='inquilinos')),
    url(r'^contrato/' , include('contratos.urls', namespace='contratos')),
    url(r'^cobranza/', include('cobranzas.urls', namespace='cobranzas')),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
