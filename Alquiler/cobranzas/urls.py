from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CobranzaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.CobranzaDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.CobranzaCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.CobranzaUpdate.as_view(), name='edit'),
	url(r'^estadocuenta/', views.EstadoCuentaList.as_view(), name='cuenta'),
]