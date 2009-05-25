# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {'page': 'home'})

def registration(request):
    return render_to_response('registration.html', {
	    'page': 'registration',
	    'years': range(1900, 2009),
	    'months': range(1, 13),
	    'days': range(1, 32),
	    })


