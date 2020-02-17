from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)$', views.tv_show_info),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy),
]
