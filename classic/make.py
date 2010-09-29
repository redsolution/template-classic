from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from classic.models import TemplateSettings

class Make(BaseMake):
    def premake(self):
        super(Make, self).premake()
        cms_settings = CMSSettings.objects.get_settings()
        template_settings = TemplateSettings.objects.get_settings()
        cms_settings.render_to(os.path.join('..', 'templates', 'base_template.html'), 'classic/templates/base_template.html', {
            'template_settings': template_settings,
        }, 'w')

    def make(self):
        super(Make, self).make()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to(os.path.join('..', 'media', 'css', 'base.css'), 'classic/media/css/base.css', {
            'template_settings': template_settings,
        }, 'w')
        cms_settings.render_to(os.path.join('..', 'media', 'css', 'style.css'), 'classic/media/css/style.css', {
            'template_settings': template_settings,
        }, 'w')
        cms_settings.render_to(os.path.join('..', 'media', 'css', 'tinymce.css'), 'classic/media/css/tinymce.css', {
            'template_settings': template_settings,
        }, 'w')

make = Make()
