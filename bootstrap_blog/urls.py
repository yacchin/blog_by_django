from django.conf.urls import patterns, include, url
from bootstrap_blog import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import bootstrap_blog.posts.urls
import bootstrap_blog.tags.urls
import bootstrap_blog.users.urls

urlpatterns = patterns('',
                       url(r'^$',
                           include(bootstrap_blog.posts.urls)),
                       url(r'^(?P<page>\d+)/$',
                           include(bootstrap_blog.posts.urls)),
                       url(r'^posts/',
                           include(bootstrap_blog.posts.urls)),
                       url(r'^users/',
                           include(bootstrap_blog.users.urls)),
                       url(r'^tags/',
                           include(bootstrap_blog.tags.urls)),
                       )
