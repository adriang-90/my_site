from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BlogConfig(AppConfig):
    name = 'sanctuary.blog'
    verbose_name = _("Blog")

    def ready(self):
        try:
            pass
        except ImportError:
            pass
