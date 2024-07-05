from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.base.models import Currency, AboutCompany


# Register your models here.


class CurrencyAdmin(TranslationAdmin):
    """Admin view of Country model"""

    ordering = ["id"]
    search_fields = [
        "id",
        "name",
    ]
    list_display = ["id", "name", ]
    list_display_links = [
        "name",
    ]
    list_filter = [
        "name",
    ]


admin.site.register(Currency, CurrencyAdmin)


class AboutCompanyAdmin(TranslationAdmin):
    """Admin view of Country model"""

    ordering = ["id"]
    search_fields = [
        "id",
        "title",
    ]
    list_display = ["id", "title", "desc", 'phone']
    list_display_links = [
        "title",
    ]


admin.site.register(AboutCompany, AboutCompanyAdmin)
