from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MantenimientoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.MantenimientoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.MantenimientoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.MantenimientoUpdate.as_view(), name='edit'),
]