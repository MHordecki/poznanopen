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
from collections import defaultdict
from django.utils.translation import ugettext as _

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
            model.tshirt = data['tshirt']
            model.nick = data['nick']
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

def admin(request):
    user = users.get_current_user()
    if not (user and users.is_current_user_admin()):
        return HttpResponseRedirect(users.create_login_url('/admin'))

    if request.method == 'POST' and request.POST['id'] and request.POST['action']:
        id = request.POST['id']
        action = int(request.POST['action'])
        model = Form.get(id)

        model.status = action
        model.put()

    pending = []
    accepted = []
    rejected = []
    
    for x in db.GqlQuery("SELECT * FROM poznanopen_form"):
        { 1:pending, 2: accepted, 3: rejected }[x.status].append(x)

    return render_to_response('admin.html', {'page': 'admin', 'pending': pending, 'accepted': accepted, 'rejected': rejected})

def news(request, id = None):
    if news:
        pass
    else:
        return render_to_response('news.html', {'page': 'news', 'news': news})

def gallery(request):
    return render_to_response('gallery.html', {'page': 'gallery'})

def venue(request):
    return render_to_response('venue.html', {'page': 'venue'})

def team(request):
    return render_to_response('contact.html', {'page': 'contact'})

def schedule(request):
    saturday = (('8:30 - 9:00', _('Official opening ceremony')),
         ('9:00 - 10:30', _("Rubik's Cube - first round (average of 5) - 20 advance to the semifinal")),
         ('9:30 - 10:30', _("Rubik's Cube Fewest Moves - first round - 7 advance to the final round")),
         ('10:35 - 11:35', _("4x4x4 Cube - combined first round (best of 2 sub-90sec -> average of 5) - 15 advance to the semifinal")),
         ('11:40 - 12:20', _("Square-1 - combined first round (best of 2 sub-90sec -> average of 5) - 10 advance to the semifinal")),
         ('12:25 - 13:20', _("5x5x5 Cube - combined first round (best of 2 sub-140sec -> average of 5) - 7 advance to the final")),
         ('13:25 - 13:50', _("2x2x2 Cube - first round (average of 5) - 20 advance to the semifinal")),
         ('13:55 - 14:30', _("Rubik's Cube One-handed - combined first round (best of 2 sub-50sec -> average of 5) - 15 advance to the semifinal")),
         ('14:30 - 15:00', _("Break")),
         ('15:00 - 15:30', _("Rubik's Clock - combined first round (best of 2 sub-30s -> average of 5) - 5 advance to the final")),
         ('15:35 - 16:00', _("Pyraminx - combined first round (best of 2 sub-20sec -> average of 5) - 7 advance to the final")),
         ('16:05 - 16:35', _("6x6x6 Cube - combined final (best of 2 sub-300sec -> mean of 3)")),
         ('16:40 - 17:25', _("7x7x7 Cube - combined final (best of 2 sub-420sec -> mean of 3)")),
         ('17:30', _("Rubik's Cube Knock-Out - unofficial event")),
         )
    sunday = (('8:30 - 9:30', _("Rubik's Cube Fewest Moves - final")),
            ('9:00 - 9:45', _("Rubik's Cube Blindfolded - first round (best of 2, total time limit: 8 minutes) - 7 advance to the final")),
            ('9:50 - 10:20', _("Rubik's Cube - semifinal (average of 5) - 10 advance to the final")),
            ('10:25 - 10:50', _("Square-1 - semifinal (average of 5) - 5 advance to the final")),
            ('10:55 - 11:30', _("Megaminx - combined final (best of 2 sub-180s -> mean of 3)")),
            ('11:35 - 11:55', _("2x2x2 Cube - semifinal (average of 5) - 10 advance to the final")),
            ('12:00 - 12:15', _("Rubik's Clock - final (average of 5)")),
            ('12:20 - 12:45', _("4x4x4 Cube - semifinal (average of 5) - 7 advance to the final")),
            ('12:50 - 13:15', _("Rubik's Cube One-handed - semifinal (average of 5) - 7 advance to the final")),
            ('13:20 - 13:25', _("Pyraminx - final (average of 5)")),
            ('13:40 - 14:00', _("Rubik's Cube Team Solving - unofficial event")),
            ('14:00 - 14:30', _("Break")),
            ('14:30 - 14:45', _("Square-1 - final (average of 5)")),
            ('14:50 - 15:05', _("Rubik's Cube Blindfolded - final (best of 3)")),
            ('15:10 - 15:30', _("5x5x5 Cube - final (average of 5)")),
            ('15:35 - 15:45', _("2x2x2 Cube - final (average of 5)")),
            ('15:50 - 16:05', _("Rubik's Cube One-handed - final (average of 5)")),
            ('16:10 - 16:25', _("4x4x4 Cube - final (average of 5)")),
            ('16:30 - 17:00', _("Rubik's Cube - final (average of 5)")),
            ('17:00', _("Closing ceremony")),
            )
    return render_to_response('schedule.html', {'page': 'schedule', 'saturday': saturday, 'sunday': sunday})

def sponsors(request):
    return render_to_response('sponsors.html', {'page': 'sponsors'})

def thanks(request):
    return render_to_response('thanks.html', {'page': 'thanks'})

def judges(request):
    return render_to_response('judges.html', {'page': 'judges'})

class Mapper:
    def __init__(self, model, counter):
        self.model = model
        for ev in self.model.events:
            counter[ev] += 1

    def __getattr__(self, attr):
        if attr == '__getitem__':
            return None
        if attr.startswith('ev_'):
            return attr in self.model.events
        else:
            return getattr(self.model, attr)

def competitors(request):
    counter = defaultdict(int)
    query = [Mapper(x, counter) for x in db.GqlQuery("SELECT * FROM poznanopen_form WHERE status = 2")]
    query.sort(key = lambda x : x.fullname.rsplit(' ', 2)[-1])

    return render_to_response('competitors.html', {'competitors': query, 'summary': counter})

    




