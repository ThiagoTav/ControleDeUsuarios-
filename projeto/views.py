from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá Django - index')

def ola(request):
    return HttpResponse('Ola Django')
