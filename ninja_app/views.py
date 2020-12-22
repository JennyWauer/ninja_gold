from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('')
    if request.method == 'POST':