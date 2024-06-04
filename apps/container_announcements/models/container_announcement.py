from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import Currency
from apps.core.models import TimeModelMixin


class ContainerAnnouncement(TimeModelMixin):
    provider = models.ForeignKey(
        "ContainerProvider",
        on_delete=models.PROTECT,
        related_name="container_announcements",
    )

    schedule_date_from = models.DateTimeField(_("Schedule Date From"))
    schedule_date_to = models.DateTimeField(_("Schedule Date To"))
    price = models.PositiveBigIntegerField(default=0)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL, blank=True, null=True,
        related_name="container_announcements_from_city",
    )
    is_by_agreement = models.BooleanField(default=False)
    from_city = models.ForeignKey(
        "City",
        on_delete=models.PROTECT,
        related_name="container_announcements_from_city",
    )
    to_city = models.ForeignKey(
        "City",
        on_delete=models.PROTECT,
        related_name="container_announcements_to_city",
    )

    container_type = models.ForeignKey(
        "ContainerType",
        on_delete=models.PROTECT,
        related_name="container_announcements",
    )
    container_form_type = models.ForeignKey(
        "ContainerFormType",
        on_delete=models.PROTECT,
        related_name="container_announcements",
    )

    shipping_type = models.ForeignKey(
        "ShippingType",
        on_delete=models.PROTECT,
        related_name="container_announcements",
    )

    search_fields = [
        "id",
        "provider",
        "schedule_date_from__gte",
        "schedule_date_to__lte",
        "from_city",
        "to_city",
        "container_type",
        "container_form_type",
        "shipping_type",
    ]

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "container_announcements"
        verbose_name = _("Container Announcement")
        verbose_name_plural = _("Container Announcements")

    def __str__(self):
        return "%s" % self.id
