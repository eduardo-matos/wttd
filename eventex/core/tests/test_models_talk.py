# coding: utf-8

from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk1 = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time='10:00'
        )

        self.talk2 = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time='13:00'
        )

    def test_create(self):
        self.assertEqual(2, Talk.objects.all().count())

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk1))

    def test_speakers(self):
        'Talk has many speakers and vice-versa'
        self.talk1.speakers.create(
                name='Eduardo Matos',
                slug='eduardo-matos',
                url='http://eduardodematos.com'
            )

        self.assertEqual(1, self.talk1.speakers.count())

    def test_talks_by_period(self):
        '''
        morning method must return only talks in the morning and
        afternoon talks mus return only talks in the afternoon
        '''
        self.assertEqual(1, Talk.morning.count())
        self.assertEqual(1, Talk.afternoon.count())