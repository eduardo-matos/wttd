# coding: utf-8

from django.contrib.auth import get_user_model
from eventex.profile.models import Profile

_User = get_user_model()

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            ''' Parece um e-mail '''
            kwargs = {'email': username}
        elif username.isdigit():
            ''' Parece um CPF '''
            kwargs = {'cpf': username}
        else:
            ''' Não parece e-mail nem CPF. Deve ser o username '''
            kwargs = {'username': username}

        try:
            if 'cpf' in kwargs:
                try:
                    profile = Profile.objects.get(cpf=kwargs['cpf'])
                except Profile.DoesNotExist:
                    raise _User.DoesNotExist

                user = profile.user
            else:
                user = _User.objects.get(**kwargs)

            if user.check_password(password):
                return user
        except _User.DoesNotExist:
            return None
 
    def get_user(self, user_id):
        try:
            return _User.objects.get(pk=user_id)
        except _User.DoesNotExist:
            return None