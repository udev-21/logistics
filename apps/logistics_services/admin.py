from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from apps.logistics_services.models.services import *
from django.utils.html import format_html


class LogisticsServiceImageAdmin(admin.TabularInline):
    model = LogisticsServiceImage
    fields = (
        "image",
        "image_tag",
    )
    readonly_fields = ("image_tag",)


@admin.register(LogisticsServiceType)
class LogisticsServiceTypeAdmin(TranslationAdmin):
    pass


@admin.register(LogisticsService)
class LogisticsServiceAdmin(TranslationAdmin):
    inlines = [LogisticsServiceImageAdmin]
    list_display = [
        "id",
        "name",
        "description",
        "service_type",
        "phone",
        "site",
        "telegram",
        "instagram",
        "watsapp",
    ]
    search_fields = ["name", "description", "phone", "site"]
    list_filter = ["service_type", "phone", "site", "name"]
    fieldsets = [
        (
            "Logistics Service",
            {
                "fields": (
                    "name",
                    "description",
                    "service_type",
                    "phone",
                    "site",
                    "telegram",
                    "instagram",
                    "watsapp",
                )
            },
        ),
    ]
