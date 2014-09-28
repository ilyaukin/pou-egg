from django.conf.urls import patterns, include, url
from egg import views

__author__ = 'ilya'

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<egg_id>\d+)/$', views.egg, name='egg'),
                       url(r'^hit/(?P<egg_id>\d+)/$', views.hit, name='hit'),
)