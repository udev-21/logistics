from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from apps.container_announcements.models import *


class ContainerAnnouncementAdmin(admin.ModelAdmin):
    """Admin view of ContainerAnnouncement model"""

    ordering = ["id"]
    search_fields = [
        "id",
    ]
    list_display = [
        "id",
        "provider",
        "schedule_date_from",
        "schedule_date_to",
        "shipping_type",
    ]
    list_display_links = [
        "id",
    ]
    list_filter = [
        "schedule_date_from",
        "schedule_date_to",
        "from_city",
        "to_city",
        "container_type",
        "container_form_type",
        "provider",
        "shipping_type",
        "created_at",
    ]
    fieldsets = [
        (
            "Container Announcement",
            {
                "fields": (
                    "provider",
                    "schedule_date_from",
                    "schedule_date_to",
                    "from_city",
                    "to_city",
                    "container_type",
                    "container_form_type",
                    "shipping_type",
                )
            },
        ),
    ]


class ContainerTypeAdmin(TranslationAdmin):
    """Admin view of ContainerType model"""

    ordering = ["id"]
    search_fields = [
        "id",
    ]
    list_display = ["id", "name"]
    list_display_links = [
        "id",
        "name",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Container Type",
            {
                "fields": (
                    "id",
                    "name",
                )
            },
        ),
    ]
    # pass


class ShippingTypeAdmin(TranslationAdmin):
    """Admin view of ShippingType model"""

    ordering = ["id"]
    search_fields = [
        "id",
    ]
    list_display = ["id", "name"]
    list_display_links = [
        "id",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Shipping Type",
            {"fields": ("name",)},
        ),
    ]


class ContainerFormTypeAdmin(TranslationAdmin):
    """Admin view of ContainerType model"""

    ordering = ["id"]
    search_fields = [
        "id",
    ]
    list_display = ["id", "name"]
    list_display_links = [
        "id",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Container Form Type",
            {"fields": ("name",)},
        ),
    ]


class CountryAdmin(TranslationAdmin):
    """Admin view of Country model"""

    ordering = ["id"]
    search_fields = [
        "id",
        "name",
    ]
    list_display = ["id", "name"]
    list_display_links = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Container Type",
            {"fields": ("name",)},
        ),
    ]


class CityAdmin(TranslationAdmin):
    """Admin view of Country model"""

    ordering = ["id"]
    search_fields = [
        "id",
        "name",
    ]
    list_display = ["id", "name", "country"]
    list_display_links = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Container Type",
            {
                "fields": (
                    "name",
                    "country",
                )
            },
        ),
    ]


class ContainerProviderAdmin(TranslationAdmin):
    """Admin view of ContainerProvider model"""

    ordering = ["id"]
    search_fields = [
        "id",
        "name",
    ]
    list_display = ["id", "name"]
    list_display_links = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    fieldsets = [
        (
            "Container Provider",
            {
                "fields": (
                    "name",
                    "description",
                    "phone",
                    "site",
                )
            },
        ),
    ]


admin.site.register(ContainerAnnouncement, ContainerAnnouncementAdmin)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(ShippingType, ShippingTypeAdmin)
admin.site.register(ContainerFormType, ContainerFormTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ContainerProvider, ContainerProviderAdmin)


# class UserAdmin(BaseUserAdmin):
#     """Admin view of User model"""

#     ordering = ["username"]
#     search_fields = [
#         "username",
#         "email",
#         "first_name",
#         "last_name",
#         "middle_name",
#         "phone",
#     ]
#     list_display = [
#         "id",
#         "username",
#         "first_name",
#         "last_name",
#         "middle_name",
#         "phone",
#         "is_active",
#         "is_superuser",
#     ]
#     list_display_links = [
#         "username",
#         "first_name",
#         "last_name",
#         "middle_name",
#         "phone",
#     ]
#     list_filter = ["is_active", "is_superuser"]
#     fieldsets = [
#         ("Credentials", {"fields": ("username", "password")}),
#         (
#             "Personal Information",
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "middle_name",
#                     "phone",
#                     "birth_date",
#                     "passport_sn",
#                     "passport_given_by",
#                     "passport_expire_date",
#                     "position",
#                     "gender",
#                 )
#             },
#         ),
#         (
#             "Extra Information",
#             {
#                 "fields": (
#                     "avatar",
#                     "address",
#                     "language",
#                     "organization",
#                     "country",
#                     "region",
#                     "district",
#                     "type",
#                 )
#             },
#         ),
#         (
#             "Notifications",
#             {
#                 "fields": (
#                     "notification",
#                     "unsubscribe_reason",
#                 )
#             },
#         ),
#         (
#             "Permissions",
#             {"fields": ("is_active", "is_superuser", "groups", "user_permissions")},
#         ),
#     ]
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2"),
#             },
#         ),
#     )
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )
