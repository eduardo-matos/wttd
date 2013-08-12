# coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime, timedelta
from eventex.core.models import Speaker


def homepage(request):
    return render_to_response('homepage.html')

def speaker_detail(request, slug):
    s = get_object_or_404(Speaker, slug=slug)
    return render_to_response('core/speaker_detail.html', {'speaker': s})

def talk_list(request):
    return render_to_response('core/talk_list.html')
    