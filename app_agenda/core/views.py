from django.shortcuts import render, redirect
from core.models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos!')

    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    # evento = Eventos.objects.get(id=1)
    # usuario = request.user
    usuario = request.user
    eventos = Eventos.objects.filter(usuario=usuario)
    # eventos = Eventos.objects.all()
    # evento = Eventos.objects.filter(usuario=usuario)
    dados = {'eventos' : eventos}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def eventos(request):
    id_evento = request.GET.get('id')
    # print(id_evento)
    dados = {}

    if id_evento:
        dados['eventos'] = Eventos.objects.get(id=id_evento)

    return render(request, 'eventos.html', dados)

@login_required(login_url='/login/')
def submit_eventos(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        id_evento = request.POST.get('id_evento')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user

        if id_evento:
            # Eventos.objects.filter(id=id_evento).update(titulo=titulo,
            #                                            data_evento=data_evento,
            #                                            descricao=descricao)

            evento = Eventos.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()

        else:
            Eventos.objects.create(titulo=titulo,
                                   data_evento=data_evento,
                                   descricao=descricao,
                                   usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    #Eventos.objects.filter(id=id_evento).delete()
    evento = Eventos.objects.get(id=id_evento)

    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')