# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/filebrowser/', include(site.urls)), 
    url(r'^', include('userx.urls')), 
]
