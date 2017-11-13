# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime

from random import randint

import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process(request):
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    building = request.POST['building']

    if building == 'farm':
        gold = random.randrange(10,21)
        request.session['activities'].append({'activity':"Earned {} gold from the {}!".format(gold,building), 'class':'win', 'date':time})

    elif building == 'cave':
        gold = random.randrange(5,11)
        request.session['activities'].append({'activity':"Earned {} gold from the {}!".format(gold,building), 'class':'win', 'date':time})

    elif building == 'house':
        gold = random.randrange(2,6)
        request.session['activities'].append({'activity':"Earned {} gold from the {}!".format(gold,building), 'class':'win', 'date':time})

    elif building == 'casino':
        gold = random.randrange(-50,51)
        if gold < 0:
            request.session['activities'].append({'activity':"You entered a {} and lost {} gold... ouch...".format(building,gold), 'class':'loss', 'date':time})
        if gold >= 0:
            request.session['activities'].append({'activity':"You entered a {} and earned {} gold".format(building, gold), 'class':'win', 'date':time})
    
    request.session['gold'] += gold
    return redirect('/')

def restart(request):
    request.session.pop('gold')
    while 'activities' in request.session:
        request.session.pop('activities')
    # for key in request.session.keys():
    #     del request.session[key]
    # request.session['gold'] = 0
    # request.session['activities'] = []
    return redirect('/')




    return redirect('index')

