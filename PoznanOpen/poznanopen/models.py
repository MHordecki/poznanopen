# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django import forms

class News(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add = True)

class Form(db.Model):
    fullname = db.StringProperty()
    country = db.StringProperty()
    city = db.StringProperty()
    wcaid = db.StringProperty()
    born = db.DateProperty()
    email = db.StringProperty()
    nick = db.StringProperty()
    tshirt = db.StringProperty()

    events = db.StringListProperty()

    accomodation = db.BooleanProperty()

    created = db.DateTimeProperty(auto_now_add = True)
    status = db.IntegerProperty()

class RegistrationForm(forms.Form):
    bornday = forms.ChoiceField(choices = zip(range(1, 32), range(1, 32)))
    bornmonth = forms.ChoiceField(choices = zip(range(1, 13), range(1, 13)))
    bornyear = forms.ChoiceField(choices = zip(range(1900, 2009), range(1900, 2009)))

    tshirt = forms.ChoiceField(choices = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')))

    fullname = forms.CharField(required = True)
    country = forms.CharField(required = True)
    city = forms.CharField(required = True)
    wcaid = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    nick = forms.CharField(required = False)

    ev_333 = forms.BooleanField(required = False)
    ev_333oh = forms.BooleanField(required = False)
    ev_333bld = forms.BooleanField(required = False)
    ev_333fm = forms.BooleanField(required = False)
    ev_222 = forms.BooleanField(required = False)
    ev_444 = forms.BooleanField(required = False)
    ev_555 = forms.BooleanField(required = False)
    ev_666 = forms.BooleanField(required = False)
    ev_777 = forms.BooleanField(required = False)
    ev_minx = forms.BooleanField(required = False)
    ev_pyr = forms.BooleanField(required = False)
    ev_sq1 = forms.BooleanField(required = False)
    ev_clock = forms.BooleanField(required = False)

    accomodation = forms.BooleanField(required = False)
    



