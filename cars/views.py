from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')
        message = request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'service': service,
            'date': date,
            'message': message
        }
        # print(data)
        message = '''
        Name: {}

        Service: {}

        Date: {}

        Message: {}

        From: {}
        '''.format(data['name'], data['service'], data['date'], data['message'], data['email'])
        print(message)
        send_mail(
           name, message, '', ['cashforcars502@gmail.com']
        )
        messages.success(request, 'Thank You! Your message has been sent!')
        return HttpResponseRedirect(reverse("index"))
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
