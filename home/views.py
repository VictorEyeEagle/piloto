# home/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'home/sobre.html')

def contato(request):
    return render(request, 'home/contato.html')