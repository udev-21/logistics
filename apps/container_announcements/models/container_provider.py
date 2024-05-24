from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin
from phonenumber_field.modelfields import PhoneNumberField


class ContainerProvider(TimeModelMixin):

    name = models.CharField(_("Name"), max_length=255)

    description = models.TextField(_("Description"), blank=True, null=True)

    phone = PhoneNumberField(_("Phone"), blank=False, null=False)
    site = models.CharField(_("Site"), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "container_providers"
        verbose_name = _("Container Provider")
        verbose_name_plural = _("Container Providers")

    def __str__(self):
        return "%s" % self.name
