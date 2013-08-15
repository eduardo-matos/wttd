# coding: utf-8

from django.test import TestCase
from eventex.core.models import Media, Talk

class MediaModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time='10:00'
        )

        self.media = Media.objects.create(
            kind='YT',
            media_id='abc123',
            title=u'Video',
            talk=self.talk
        )

    def test_create(self):
        self.assertEqual(1, Media.objects.all().count())

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django - Video', unicode(self.media))
