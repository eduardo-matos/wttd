# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk

class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Eduardo Matos', slug='eduardo-matos',
            url='http://eduardodematos.com/', description='desenvolvedor')

        t1 = Talk.objects.create(description=u'Descrição da palestra', title=u'Título da palestra', start_time='10:00')
        t2 = Talk.objects.create(description=u'Descrição da palestra', title=u'Título da palestra', start_time='14:00')

        s.talk_set.add(t1)
        s.talk_set.add(t2)

        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'/talk/1')
        self.assertContains(self.resp, u'/talk/2')
        self.assertContains(self.resp, u'/speaker/eduardo-matos', 2)
        self.assertContains(self.resp, u'desenvolvedor', 2)
        self.assertContains(self.resp, u'Eduardo Matos', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)

    def test_morning_talk_in_context(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talk_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)
