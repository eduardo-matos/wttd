# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk, Media

class TalkListDetailTest(TestCase):
    def setUp(self):
        talk = Talk.objects.create(description=u'Descrição da palestra', title=u'Título da palestra', start_time='10:00')
        media = Media.objects.create(title='Dummy title', media_id='abc123', kind='YT', talk=talk)
        self.resp = self.client.get(r('core:talk_detail', args=[talk.pk]))

    def test_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_404(self):
        resp = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, resp.status_code)
        
    def test_html(self):
        self.assertContains(self.resp, u'Descrição da palestra')
        self.assertContains(self.resp, u'Título da palestra')
        self.assertContains(self.resp, u'10:00')

    def test_media_in_content(self):
        self.assertContains(self.resp, 'abc123')
        self.assertContains(self.resp, 'Dummy title')