from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ deve retornar codigo 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/inscricao.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML deve conter csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context mus have subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Eduardo de Matos', cpf='11122233380', email='edu@matos.com', phone='21-32456789')
        self.resp = self.client.post(r('subscriptions:inscricao'), data)

    def test_post(self):
        'Valid post should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save_info(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Eduardo de Matos', cpf='123456789012', email='edu@matos.com', phone='21-32456789')
        self.resp = self.client.post(r('subscriptions:inscricao'), data)

    def test_post(self):
        'Invalid post should not redirect'
        self.assertNotEqual(302, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())