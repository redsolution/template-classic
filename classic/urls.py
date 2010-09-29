# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from classic.admin import TemplateSettingsAdmin
admin_instance = TemplateSettingsAdmin()

urlpatterns = patterns('',
    url(r'^$', admin_instance.change_view, name='template_index'),
)
