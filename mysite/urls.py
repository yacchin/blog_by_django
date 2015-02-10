from django.conf.urls import patterns, include, url
from django.contrib import admin

import bootstrap_blog.urls

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^bootstrap_blog/',
                           include(bootstrap_blog.urls,
                                   namespace="bootstrap_blog")),
                       )
