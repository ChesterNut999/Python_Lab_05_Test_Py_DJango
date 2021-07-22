from django.shortcuts import render, HttpResponse

# Create your views here.

def teste(request, nome, idade):
    return HttpResponse('<h1>Hello {}! Você tem {} anos de idade.</h1>'.format(nome, idade))