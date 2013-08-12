from django.test import TestCase
from eventex.core.models import Speaker

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = 'Eduardo Matos',
            url = 'http://eduardodematos.com',
            description = 'desenvolvedor',
            slug = 'eduardo-matos'
        )

    def test_create(self):
        self.assertEqual(1, Speaker.objects.all().count())

    def test_unicode(self):
    	self.assertEqual('Eduardo Matos', unicode(self.speaker))
