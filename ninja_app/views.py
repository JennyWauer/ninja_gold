from django.shortcuts import render, redirect

import random

import time

# Create your views here.
def home(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['activity_log'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        click_time = time.strftime("%H:%M:%S",time.localtime(time.time()))
        if request.POST['location'] == 'farm':
            gold = random.randint(10, 20)
            request.session['counter'] += gold
            statement = "Earned " + str(gold) + " from the " + request.POST['location'] + "! (" + str(click_time) + ")"
            request.session['activity_log'].append(statement)
        if request.POST['location'] == 'cave':
            gold = random.randint(5, 10)
            request.session['counter'] += gold
            statement = "Earned " + str(gold) + " from the " + request.POST['location'] + "! (" + str(click_time) + ")"
            request.session['activity_log'].append(statement)
        if request.POST['location'] == 'house':
            gold = random.randint(2, 5)
            request.session['counter'] += gold
            statement = "Earned " + str(gold) + " from the " + request.POST['location'] + "! (" + str(click_time) + ")"
            request.session['activity_log'].append(statement)
        if request.POST['location'] == 'casino':
            gold = random.randint(-50, 50)
            request.session['counter'] += gold
            if gold >= 0:
                statement = "Earned " + str(gold) + " from the " + request.POST['location'] + "! (" + str(click_time) + ")"
                request.session['activity_log'].append(statement)
            else:
                statement = "Entered a casino and lost " + str(gold) + " gold... Ouch... (" + str(click_time) + ")"
                request.session['activity_log'].append(statement)
        return redirect('/')