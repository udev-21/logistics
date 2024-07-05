from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class AboutCompany(TimeModelMixin):
    title = models.CharField(_("title"), max_length=255)
    desc = models.TextField(_("description"))
    image = models.ImageField(upload_to='about_company', default='/about_company/default.png')
    phone = models.CharField(max_length=20)
    telegram_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.title
