from django.conf.urls import include, url
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^$', post_list, name='home'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^create$', post_create, name='create'),
    url(r'^update/(?P<slug>[\w-]+)/$', post_update, name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/$', post_delete, name='delete')
]


