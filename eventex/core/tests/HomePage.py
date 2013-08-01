from django.test import TestCase

class HomePageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        'GET / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        'Homepage deve usar template homepage.html'
        self.assertTemplateUsed(self.resp, 'homepage.html')
