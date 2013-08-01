# Create your views here.
from django.shortcuts import render


def inscricao(request):
    return render(request, 'subscriptions/inscricao.html')