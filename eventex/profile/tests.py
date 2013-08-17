"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from eventex.profile.models import Profile


_User = get_user_model()

class UserProfileTest(TestCase):
    def setUp(self):
    	self.user = _User.objects.create(username='eduardo', password='123', email='some@email.com')
    	self.userProfile = Profile.objects.create(cpf=12345678901, user=self.user)

    def test_access_cpf_from_user(self):
    	self.assertEqual(12345678901, self.user.profile.cpf)