from django.test import TestCase
from django.contrib.auth.models import User
from eventex.profile.models import Profile

class MyAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='e@duardo', email='edu@matos.com', password='123')
        self.profile = Profile.objects.create(cpf=12345678901, user=self.user)

    def test_can_login_with_username(self):
        assert self.client.login(username=self.user.username, password='123')

    def test_can_login_with_email(self):
        assert self.client.login(username=self.user.email, password='123')

    def test_cant_login_with_incorrect_creadentials(self):
        assert not self.client.login(username=self.user.username, password='321')
        assert not self.client.login(username=self.user.email, password='321')

    def test_can_login_with_user_cpf(self):
    	assert self.client.login(username='12345678901', password='123')

    def test_cant_login_with_incorrect_cpf(self):
    	assert not self.client.login(username='1', password='123')


