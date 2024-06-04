from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeModelMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe


def logistics_image_upload_location(instance, filename):
    return f"logistics_services/{filename}"


class LogisticsService(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))

    service_type = models.ForeignKey(
        "LogisticsServiceType",
        on_delete=models.PROTECT,
        related_name="services",
    )
    phone = PhoneNumberField(_("Phone"), blank=False, null=False)
    site = models.CharField(_("Site"), max_length=255, blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=logistics_image_upload_location,
                              default='logistics_services/default.png')
    telegram = models.CharField(_("Telegram"), max_length=255, blank=True, null=True)
    instagram = models.CharField(_("Instagram"), max_length=255, blank=True, null=True)
    watsapp = models.CharField(_("Watsapp"), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "logistics_services"
        verbose_name = _("Logistics Service")
        verbose_name_plural = _("Logistics Services")

    def __str__(self):
        return "%s" % self.name


class LogisticsServiceType(TimeModelMixin):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "logistics_service_types"
        verbose_name = _("Logistics Service Type")
        verbose_name_plural = _("Logistics Service Types")

    def __str__(self):
        return "%s" % self.name


class LogisticsServiceImage(TimeModelMixin):
    service = models.ForeignKey(
        "LogisticsService",
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(_("Image"), upload_to=logistics_image_upload_location)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        ordering = ["id", "created_at"]
        db_table = "logistics_service_images"
        verbose_name = _("Logistics Service Image")
        verbose_name_plural = _("Logistics Service Images")

    def __str__(self):
        # generate image url with domain
        return "%s" % self.image.url
