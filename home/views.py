from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context ={
    #     "variable1": "satyam",
    #     "variable2": "satyam test"
    # }
    # return HttpResponse("this is home")
    # messages.success(request,"this is test message")
    return render (request, 'index.html')

def about(request):
    # return HttpResponse("this is about")

    return render (request, 'about.html')

def services(request):
    # return HttpResponse("this is services")
    return render (request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, contact=contact, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    # return HttpResponse("this is contact")
    return render (request, 'contact.html')