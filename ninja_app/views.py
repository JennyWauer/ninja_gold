from django.shortcuts import render, redirect

import random

# Create your views here.
def home(request):
    return render(request, 'index.html')

def process_money(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if request.method == 'GET':
        return redirect('')
    elif request.method == 'POST':
        if request.POST['location'] == 'farm':
            gold = random.randint(10, 20)*1
            request.session['counter'] += gold
        elif request.POST['location'] == 'cave':
            gold = random.randint(5, 10)*1
            request.session['counter'] += gold
        elif request.POST['location'] == 'house':
            gold = random.randint(2, 5)*1
            request.session['counter'] += gold
        elif request.POST['location'] == 'casino':
            gold = random.randint(0, 50)*1
            request.session['counter'] += gold