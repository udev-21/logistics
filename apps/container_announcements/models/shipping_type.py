from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class ShippingType(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)
    bg_color = models.CharField(_("Color"), max_length=255)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "shipping_types"
        verbose_name = _("Shipping Type")
        verbose_name_plural = _("Shipping Types")

    def __str__(self):
        return "%s" % self.name
