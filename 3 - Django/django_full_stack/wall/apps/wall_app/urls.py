# from django.conf.urls import url
# from . import views

# urlpatterns = [
# 	url(r'^$', views.index),
# 	url(r'^post_message$', views.index),
# ]


from django.conf.urls import url
from . import views

urlpatterns = [
	#from the login app
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
    url(r'^users/register$', views.register),
    url(r'^users/login$', views.login),
    url(r'^logout$', views.logout),
	#for the wall app
	url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete/(?P<message_id>\d+)$', views.delete_message),
]