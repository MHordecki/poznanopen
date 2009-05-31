# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from models import News, Form, RegistrationForm
from google.appengine.api import users
from google.appengine.ext import db
from django.conf import settings
from ragendja.auth.decorators import staff_only
import datetime

def index(request):
    return render_to_response('index.html', {'page': 'home'})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model = Form()
            model.fullname = data['fullname']
            model.wcaid = data['wcaid']
            model.country = data['country']
            model.city = data['city']
            model.email = data['email']
            model.accomodation = data['accomodation']
            model.born = datetime.date(int(data['bornyear']), int(data['bornmonth']), int(data['bornday']))
            model.events = [str(ev) for ev in data if ev.startswith('ev_') and data[ev] == True]
            model.status = 1
            model.put()

            return HttpResponseRedirect('/thanks')
    else:
        form = RegistrationForm()

    return render_to_response('registration.html', {
        'form': form,
        'page': 'registration',
        'years': range(1900, 2009),
        'months': range(1, 13),
        'days': range(1, 32),
        })

def news(request, id = None):
    if news:
        pass
    else:
        return render_to_response('news.html', {'page': 'news', 'news': news})

def gallery(request):
    pass

def venue(request):
    return render_to_response('venue.html', {'page': 'venue'})

def contact(request):
    return render_to_response('contact.html', {'page': 'contact'})

def schedule(request):
    return render_to_response('schedule.html', {'page': 'schedule'})

def sponsors(request):
    return render_to_response('sponsors.html', {'page': 'sponsors'})

def thanks(request):
    return render_to_response('thanks.html', {'page': 'thanks'})

class Mapper:
    def __init__(self, model):
        self.model = model

    def __getattr__(self, attr):
        if attr == '__getitem__':
            return None
        if attr.startswith('ev_'):
            return attr in self.model.events
        else:
            return getattr(self.model, attr)

def competitors(request):
    query = (Mapper(x) for x in db.GqlQuery("SELECT * FROM poznanopen_form WHERE status = 2"))

    return render_to_response('competitors.html', {'competitors': query})

    




