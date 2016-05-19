from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.LoteList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.LoteDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.LoteCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.LoteUpdate.as_view(), name='edit'),
	url(r'^transaccion/', views.LoteTransaccionContratoList.as_view(), name='transaction'),
]