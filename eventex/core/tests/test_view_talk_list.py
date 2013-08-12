# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r

class TalkListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'/palestra/1')
        self.assertContains(self.resp, u'/palestra/2')
        self.assertContains(self.resp, u'/palestrantes/eduardo-matos', 2)
        self.assertContains(self.resp, u'desenvolvedor', 2)
        self.assertContains(self.resp, u'Eduardo Matos', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)
