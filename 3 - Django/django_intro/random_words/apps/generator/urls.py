from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^random_word$', views.index),
    url(r'^generate$', views.generate),
    url(r'^reset$', views.reset),
]