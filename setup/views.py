from django.shortcuts import render

def homepage(request):
    nome = 'Fulano'
    pessoa = {
        'nome': 'Matheus',
        'idade': 23,
        'cidade': 'Londrina'
    }
    return render(request, 'home.html', {'nome': nome, 'pessoa':pessoa})

def about(request):
    frutas = ['Maçã', 'Perâ', 'Banana', 'Tomate', 'Kiwi', 'Uva', 'Maracujá', 'Laranja']
    return render(request,'about.html', {'frutas': frutas})