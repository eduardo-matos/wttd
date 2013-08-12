from django.db import models

class EmailContactManager(models.Manager):
    def get_query_set(self):
        qs = super(EmailContactManager, self).get_query_set()
        return qs.filter(kind='E')

class PhoneContactManager(models.Manager):
    def get_query_set(self):
        qs = super(PhoneContactManager, self).get_query_set()
        return qs.filter(kind='P')

class FaxContactManager(models.Manager):
    def get_query_set(self):
        qs = super(FaxContactManager, self).get_query_set()
        return qs.filter(kind='F')
