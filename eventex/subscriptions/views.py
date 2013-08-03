# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def inscricao(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/inscricao.html', {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/inscricao.html', {'form': form})

    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)


