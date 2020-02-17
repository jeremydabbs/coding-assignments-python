from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^add_book$', views.add_book),
    url(r'^add_author$', views.add_author),
    url(r'^books/(?P<book_id>\d+)$', views.show_books),
    url(r'^authors/(?P<author_id>\d+)$', views.show_authors),
    url(r'^authors/update/(?P<book_id>\d+)$', views.update_author),
    url(r'^books/update/(?P<author_id>\d+)$', views.update_book),
    url(r'^books/(?P<book_id>\d+)/delete$', views.delete_book),
    url(r'^authors/(?P<author_id>\d+)/delete$', views.delete_author),
]



# # from class example
# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^user/create$', view.create_user), #good form is starting url with model name, keep naming consistent
#     url(r'^user/(?P<user_id>\d+)/delete$', views.delete_user),
# ]