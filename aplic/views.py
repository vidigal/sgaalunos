from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo! Você está na página principal do SCA.")

def teste(request):
    return HttpResponse("isso é um teste")