from django.shortcuts import render
from django.http import HttpResponse

def myusers(request):
    return HttpResponse('Olá Django')

def contact(request):
    return HttpResponse('Contatos')

