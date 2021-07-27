from django.shortcuts import render
from core.models import Eventos

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    # evento = Eventos.objects.get(id=1)
    usuario = request.user
    eventos = Eventos.objects.all()
    # evento = Eventos.objects.filter(usuario=usuario)
    dados = {'eventos' : eventos}
    return render(request, 'agenda.html', dados)

