# Create your views here.
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def inscricao(request):
    return render(request, 'subscriptions/inscricao.html', {'form': SubscriptionForm()})