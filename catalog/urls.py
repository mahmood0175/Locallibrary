from django.conf.urls import re_path 
from . import views

app_name='catalog'
urlpatterns = [
    re_path(r'^$', views.index,  name='index'),
    re_path(r'^books$', views.BookListView.as_view(),  name='books'),
    re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(),  name='book-detail'),  
]
