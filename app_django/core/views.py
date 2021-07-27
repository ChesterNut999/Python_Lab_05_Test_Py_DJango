from django.shortcuts import render, HttpResponse

# Create your views here.

def teste(request, nome, idade):
    return HttpResponse('<h1>Hello {}! Você tem {} anos de idade.</h1>'.format(nome, idade))

def calcula(request, num1, num2):
    total_soma = num1 + num2
    total_subtracao = num1 - num2
    total_multiplicacao = num1 * num2
    total_divisao: float = num1 / num2

    return HttpResponse(
        '<h1>A soma de {} com {} é igual a {}'.format(num1, num2, total_soma) +
        '<p>A subtração de {} por {} é igual a {}</p>'.format(num1, num2, total_subtracao) +
        '<p>A multiplicação de {} por {} é igual a {}</p>'.format(num1, num2, total_multiplicacao) +
        'A divisão de {} por {} é igual a {}</h1>'.format(num1, num2, total_divisao)
    )
