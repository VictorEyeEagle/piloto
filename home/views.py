from django.shortcuts import render
import datetime


def index(request):
    return render(request, "index.html")
def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def exibir_item(request,id):
    return render(request,'exibir_item.html',{'id':id})

