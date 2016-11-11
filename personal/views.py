from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you want to contact me, send me an email','maddymaster@gmail.com']})