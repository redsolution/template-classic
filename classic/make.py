from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from classic.models import TemplateSettings
import os


class Make(BaseMake):
    def premake(self):
        super(Make, self).premake()
        cms_settings = CMSSettings.objects.get_settings()
        template_settings = TemplateSettings.objects.get_settings()
        cms_settings.render_to(['..', 'templates', 'base_template.html'], 'classic/templates/base_template.html', {
            'template_settings': template_settings,
        }, 'w')

    def make(self):
        super(Make, self).make()
        cms_settings = CMSSettings.objects.get_settings()

        cms_settings.copy_to(
            os.path.join(cms_settings.project_dir, 'media',),
            os.path.join(os.path.dirname(__file__), 'templates', 'classic', 'media'),
            merge=True
        )
        cms_settings.copy_to(
            os.path.join(cms_settings.project_dir, 'templates',),
            os.path.join(os.path.dirname(__file__), 'templates', 'classic', 'templates'),
            merge=True
        )

make = Make()
