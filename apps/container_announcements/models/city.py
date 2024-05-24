from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin


class City(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)
    country = models.ForeignKey(
        "Country",
        on_delete=models.PROTECT,
        related_name="cities",
    )

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "cities"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return "%s" % self.name
