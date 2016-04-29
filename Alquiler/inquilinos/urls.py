from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.InquilinoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.InquilinoDetail.as_view(), name='detail'),
	url(r'^nuevo$', views.InquilinoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', views.InquilinoUpdate.as_view(), name='edit'),
	url(r'^borrar/(?P<pk>\d+)$', views.InquilinoDelete.as_view(), name='delete'),
]