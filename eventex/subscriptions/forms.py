# coding: utf-8

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription

def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    elif len(value) != 11:
        raise ValidationError(_(u'CPF deve conter 11 caracteres'))

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = name.split()
        words = map(lambda w: w.capitalize(), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise ValidationError(_(u'Informe seu telefone ou seu e-mail'))

        return self.cleaned_data
