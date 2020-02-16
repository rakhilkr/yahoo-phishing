from django.shortcuts import render,HttpResponseRedirect
import datetime
from twilio.rest import Client
from django.core.mail import EmailMessage


def fun1(request):
    return render(request, 'home.html')


def fun2(request):
    return render(request, 'contact.html')


def fun3(request):
    return render(request, 'gallery.html')