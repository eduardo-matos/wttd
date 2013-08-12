from django.test import TestCase
from eventex.core.models import Speaker, Contact

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


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = 'Eduardo Matos',
            url = 'http://eduardodematos.com',
            description = 'desenvolvedor',
            slug = 'eduardo-matos'
        )

    def test_email(self):
        contato = Contact.objects.create(
            speaker = self.speaker,
            kind = 'E',
            value = 'edu@matos.com'
        )

        self.assertEqual(1, Contact.objects.all().count())

    def test_phone(self):
        contato = Contact.objects.create(
            speaker = self.speaker,
            kind = 'P',
            value = '21-22554477'
        )

        self.assertEqual(1, Contact.objects.all().count())

    def test_faz(self):
        contato = Contact.objects.create(
            speaker = self.speaker,
            kind = 'F',
            value = 'edu@matos.com'
        )

        self.assertEqual(1, Contact.objects.all().count())

    def test_unicode(self):
        "Contact unicode must be it's value"
        contato = Contact.objects.create(
            speaker = self.speaker,
            kind = 'F',
            value = 'edu@matos.com'
        )

        self.assertEqual('edu@matos.com', unicode(contato))