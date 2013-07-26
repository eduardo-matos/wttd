# coding: utf-8

from django.shortcuts import render_to_response
from datetime import datetime, timedelta


def homepage(request):
    return render_to_response('homepage.html')
