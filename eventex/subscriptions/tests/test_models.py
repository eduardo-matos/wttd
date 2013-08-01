from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Eduardo Matos',
            cpf = '12345678901',
            email = 'eduardo@matos.com',
            phone = '21-99887766'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Eduardo Matos', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name = 'Eduardo',
            cpf = '12345678901',
            email = 'eduardo@matos.com',
            phone = '21-99887766'            
        )

    def test_cpf_unique(self):
        s = Subscription(
            name = 'Eduardo',
            cpf = '12345678901',
            email = 'outro@matos.com',
            phone = '21-99887766' 
        )

        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        s = Subscription(
            name = 'Eduardo',
            cpf = '11111111111',
            email = 'eduardo@matos.com',
            phone = '21-99887766' 
        )

        self.assertRaises(IntegrityError, s.save)

        
