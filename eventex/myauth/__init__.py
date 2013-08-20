from django.contrib.auth.forms import AuthenticationForm

AuthenticationForm.base_fields['username'].label = 'CPF'