# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    url = models.URLField(_('Url'))
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Descrição'), blank=True)
