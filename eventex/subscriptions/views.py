# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def inscricao(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render_to_response('subscriptions/detail.html', {'subscription': subscription})

def new(request):
    return render(request, 'subscriptions/inscricao.html', {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/inscricao.html', {'form': form})

    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)


