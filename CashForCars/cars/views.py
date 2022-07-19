from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def cashforallcars(request):
    return render(request, 'cashforallcars.html')

def cashforcars(request):
    return render(request, 'cashforcars.html')

def contact(request):
    return render(request, 'contact.html')

def getquote(request):
    return render(request, 'getquote.html')
