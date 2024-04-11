from django.shortcuts import render
from django.http import HttpResponse
from projeto.models import Question


def index(request):
    # return HttpResponse('Olá Django - index')
    # return render(request, 'index.html  ')
    return render(request, 'index.html', { 'titulo': 'Últimas Enquetes'})

def ola(request):
    # return HttpResponse('Ola Django')
    questions = Question.objects.all()
    context = {'all_questions' : questions}
    return render(request, 'projeto/questions.html', context)