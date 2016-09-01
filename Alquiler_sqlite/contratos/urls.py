from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.ContratoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.ContratoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.ContratoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.ContratoUpdate.as_view(), name='edit'),
]