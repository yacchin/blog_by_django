from django.conf.urls import patterns, url
from bootstrap_blog.posts import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^new', views.new, name='new'),
                       url(r'^(?P<page>\d+)/$', views.show, name='show'),
                       url(r'^(?P<page>\d+)/edit', views.edit, name='edit'),
                       )
