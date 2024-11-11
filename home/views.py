from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'home/sobre.html')

def contato(request):
    return render(request, 'home/contato.html')

def dia_da_semana(request, dia):
    dias_semana = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    nome_dia = dias_semana.get(dia, 'Dia inválido')  
    return render(request, 'home/diasemana.html', {'nome_dia': nome_dia})

def perfil(request, usuario):

    return render(request, 'home/perfil.html', {'usuario': usuario})
