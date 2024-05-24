from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class ContainerFormType(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "container_form_types"
        verbose_name = _("Container Form Type")
        verbose_name_plural = _("Container Form Types")

    def __str__(self):
        return "%s" % self.name
