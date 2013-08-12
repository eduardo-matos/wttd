from django.test import TestCase
from eventex.core.models import Contact, Speaker

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Eduardo Matos',
            slug='eduardo-matos',
            url='http://eduardodematos.com'
        )

        s.contact_set.add(Contact(kind='E', value='edu.de.matos@hotmail.com'),
                          Contact(kind='P', value='21-88119955'),
                          Contact(kind='F', value='21-11997733'))

    def test_emails(self):
        qs = Contact.emails.all()
        expect = ['<Contact: edu.de.matos@hotmail.com>']
        self.assertQuerysetEqual(qs, expect)

    def test_phones(self):
        qs = Contact.phones.all()
        expect = ['<Contact: 21-88119955>']
        self.assertQuerysetEqual(qs, expect)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expect = ['<Contact: 21-11997733>']
        self.assertQuerysetEqual(qs, expect)
