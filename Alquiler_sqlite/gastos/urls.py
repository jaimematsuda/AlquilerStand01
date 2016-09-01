from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.GastoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.GastoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.GastoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.GastoUpdate.as_view(), name='edit'),
]