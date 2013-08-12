from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name = 'Eduardo Matos',
            url = 'http://eduardodematos.com',
            description = 'desenvolvedor',
            slug = 'eduardo-matos'
        )

        url = r('core:speaker_detail', kwargs={'slug': s.slug})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET  should return 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        self.assertContains(self.resp, 'Eduardo Matos')
        self.assertContains(self.resp, 'desenvolvedor')
        self.assertContains(self.resp, 'eduardodematos.com')

    def test_context(self):
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)