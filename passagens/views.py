from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        contexto = {'form':form}
        return render(request, 'minha_consulta.html', contexto)

