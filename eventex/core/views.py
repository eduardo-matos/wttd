# coding: utf-8

from django.shortcuts import render
from datetime import datetime, timedelta


def homepage(request):

    # semana que vem
    data_evento = datetime.now() + timedelta(weeks=1)

    return render(request, 'homepage.html', {'data_evento': data_evento})
