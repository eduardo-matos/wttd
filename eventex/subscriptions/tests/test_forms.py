from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF must only accept digits'
        form = self.make_validated_form(cpf='1234567abvc9')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_iptional(self):
        'E-mail should be optional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_should_be_capitalized(self):
        form = self.make_validated_form(name='EDUARDO DE matos')
        self.assertEqual('Eduardo De Matos', form.cleaned_data['name'])


    def make_validated_form(self, **kwargs):
        data = dict(name='eduardo', email='edu@matos.com', cpf='12345678901', phone='21-12345678')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form