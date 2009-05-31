# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from myapp.forms import UserRegistrationForm
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    # Override the default registration form
#    url(r'^account/register/$', 'registration.views.register',
#        kwargs={'form_class': UserRegistrationForm},
#        name='registration_register'),
    (r'^$', 'poznanopen.views.index'),
    (r'^registration$', 'poznanopen.views.registration'),
    (r'^contact$', 'poznanopen.views.contact'),
    (r'^news/(?P<id>\d+)/(.*)$', 'poznanopen.views.news'),
    (r'^venue$', 'poznanopen.views.venue'),
    (r'^sponsors$', 'poznanopen.views.sponsors'),
#    (r'^schedule$', 'poznanopen.views.schedule'),
    (r'^gallery$', 'poznanopen.views.gallery'),
    (r'^thanks$', 'poznanopen.views.thanks'),
    (r'^competitors$', 'poznanopen.views.competitors'),

) + urlpatterns
