from redsolutioncms.admin import CMSBaseAdmin
from classic.models import TemplateSettings

class TemplateSettingsAdmin(CMSBaseAdmin):
    model = TemplateSettings
