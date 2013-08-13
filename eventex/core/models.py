# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    url = models.URLField(_('Url'))
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Descrição'), blank=True)

    class Meta:
        verbose_name=_('palestrante')
        verbose_name_plural=_('palestrantes')

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
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    class Meta:
        verbose_name=_('palestra')
        verbose_name_plural=_('palestras')

    def __unicode__(self):
        return self.title