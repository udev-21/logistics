from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class Currency(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        ordering = ["id", "created_at"]

    def __str__(self):
        return "%s" % self.name
