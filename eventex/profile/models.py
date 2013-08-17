from django.db import models
from django.contrib.auth import get_user_model

_User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(_User)
    cpf = models.CharField('cpf', max_length=11)
