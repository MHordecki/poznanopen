# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response

def index(request):
    request.session['django_language'] = 'pl'
    return render_to_response('index.html', {'page': 'home'})


