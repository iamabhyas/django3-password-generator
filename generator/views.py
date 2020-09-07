from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'lkjhsdihisahisdi'})

def eggs(request):
    return HttpResponse('<h1>Eggs are so testy</h1>')

def password(request):
    characters = list('abcdefghijklmnopquestruvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQURESTUVWXYZ'))

    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    password = ''
    for x in range(length):
        password += random.choice(characters)

    
    return render(request, 'generator/password.html', {'password' : password})


def about(request):
    return render(request, 'generator/about.html')

    