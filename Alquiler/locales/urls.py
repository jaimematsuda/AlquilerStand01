from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.LocalList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.LocalDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.LocalCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.LocalUpdate.as_view(), name='edit'),
	url(r'^borrar/(?P<pk>\d+)$', views.LocalDelete.as_view(), name='delete'),
]