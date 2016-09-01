from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CobranzaList.as_view(), name='list'),
	url(r'^([0-9]{2})/([0-9]{4})$', views.CobranzaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.CobranzaDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.CobranzaCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.CobranzaUpdate.as_view(), name='edit'),
	url(r'^estadocuenta/$', views.EstadoCuentaList.as_view(), name='cuenta'),
	url(r'^estadocuenta/([0-9]{2})/([0-9]{4})$', views.EstadoCuentaList.as_view(), name='cuenta'),
	#url(r'^estadocuenta/contrato/$', views.EstadoCuentaContratoList.as_view(), name='cuentacontrato'),
	url(r'^estadocuenta/contrato/([0-9]{2})/([0-9]{4})/(?P<pk>\d+)$', views.EstadoCuentaContratoList.as_view(), name='cuentacontrato'),
]