# Create your views here.
from django.shortcuts import render


def inscricao(request):
    return render(request, 'inscricao.html')