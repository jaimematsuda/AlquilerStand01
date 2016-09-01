from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CajaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.CajaDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.CajaCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.CajaUpdate.as_view(), name='edit'),
]