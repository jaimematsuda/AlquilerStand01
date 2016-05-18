from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.BancoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.BancoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.BancoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.BancoUpdate.as_view(), name='edit'),
]