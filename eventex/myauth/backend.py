from django.contrib.auth import get_user_model
from django.core.validators import validate_email, ValidationError

_User = get_user_model()

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
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
