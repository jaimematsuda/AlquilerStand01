from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.LoteList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.LoteDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.LoteCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.LoteUpdate.as_view(), name='edit'),
	url(r'^transaccion/$', views.LoteTransaccionContratoList.as_view(), name='transaction'),
	url(r'^transaccion/nueva_cobranza/$', views.LoteNuevaCobranzaCreation.as_view(), name='new_cobranza'),
	url(r'^transaccion/editar_cobranza/(?P<pk>\d+)$', views.LoteNuevaCobranzaUpdate.as_view(), name='edit_cobranza'),
	#url(r'^transaccion/nuevo_pago/([0-9]{4})-([0-9]{1})$', views.LoteNuevoPagoCreation.as_view(), name='new_Pago'),
	url(r'^transaccion/nuevo_pago$', views.LoteNuevoPagoCreation.as_view(), name='new_Pago'),
	url(r'^lotecobranza/$', views.LoteCobranzaList.as_view(), name='list_lotecobranza'),
	url(r'^lotecobranza/nueva/$', views.LoteCobranzaCreation.as_view(), name='new_lotecobranza'),
	url(r'^lotecobranza/editar/(?P<pk>\d+)$', views.LoteCobranzaUpdate.as_view(), name='edit_lotecobranza'),	
]