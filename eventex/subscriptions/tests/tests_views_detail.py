from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='eduardo',
            cpf='12345678901',
            email='edu@matos.com',
            phone='21-12345678')

        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        'GET /inscricao/1/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        'Uses tempalte'
        self.assertTemplateUsed(self.resp, 'subscriptions/detail.html')

    def test_context(self):
        self.assertIsInstance(self.resp.context['subscription'], Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'eduardo')


class DetailNotFoundTest(TestCase):
    def test_not_found(self):
        'must return 404 when subscription is not found'
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)