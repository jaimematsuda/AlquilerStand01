from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^([\w-]+)$', views.PagoList.as_view(), name='list'),
	#url(r'^([^/]+)$', views.PagoList.as_view(), name='list'),
	url(r'^([0-9]{2})/([0-9]{4})$', views.PagoList.as_view(), name='list'),
	#url(r'^$', views.PagoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.PagoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.PagoCreation.as_view(), name='new'),
	url(r'^nuevo/([0-9]{2})/([0-9]{4})$', views.PagoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.PagoUpdate.as_view(), name='edit'),
]
