# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

import wsfactory.urls

from m3 import get_app_urlpatterns
from m3_ext import workspace

admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', login_required(workspace()), name='desktop') ,
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'main.views.logout_view', name='logout'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += get_app_urlpatterns()
urlpatterns += wsfactory.urls.urlpatterns
