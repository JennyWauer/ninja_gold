from django.shortcuts import render, redirect

import random

# Create your views here.
def home(request):
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('')
    elif request.method == 'POST':
        print("Post request")