# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import EmailContactManager, PhoneContactManager, FaxContactManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    url = models.URLField(_('Url'))
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Descrição'), blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('E',_('E-mail')),
        ('P',_('Telefone')),
        ('F',_('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    objects = models.Manager()
    emails = EmailContactManager()
    phones = PhoneContactManager()
    faxes = FaxContactManager()

    def __unicode__(self):
        return self.value
