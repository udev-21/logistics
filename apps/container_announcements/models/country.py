from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class Country(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return "%s" % self.name
