from django import forms
from django.utils.translation import ugettext as _

class SubscriptionForm(forms.Form):
	name = forms.CharField(label = _('Nome'))
	cpf = forms.CharField(label = _('Cpf'))
	email = forms.EmailField(label = _('E-mail'))
	phone = forms.CharField(label = _('Telefone'))