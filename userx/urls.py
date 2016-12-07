# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import userx.views 

admin.autodiscover()

urlpatterns = (
	url(r'^$', userx.views.home_page , ),
	url(r'^do_transfer$', userx.views.ajax_transfer),
)
