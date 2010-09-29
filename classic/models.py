# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redsolutioncms.models import BaseSettings

class TemplateSettings(BaseSettings):
    THEMES = (
        ('R', _('Red')),
        ('G', _('Green')),
        ('B', _('Blue')),
    )
    theme = models.CharField(verbose_name=_('Template theme'), choices=THEMES, max_length=1, default='R')
