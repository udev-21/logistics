from django.urls import path

from api.container_announcements.views.city import CityListView
from api.container_announcements.views.country import CountryListView
from api.container_announcements.views.container_type import ContainerTypeListView
from api.container_announcements.views.container_form_type import (
    ContainerFormTypeListView,
)
from api.container_announcements.views.container_provider import (
    ContainerProviderListView,
)

from api.container_announcements.views.shipping_type import ShippingTypeListView

from api.container_announcements.views.container_announcement import (
    ContainerAnnouncementListView,
)

urlpatterns = [
    path("countries", CountryListView.as_view(), name="country-list"),
    path("cities", CityListView.as_view(), name="city-list"),
    path(
        "container-types", ContainerTypeListView.as_view(), name="container-type-list"
    ),
    path(
        "container-form-types",
        ContainerFormTypeListView.as_view(),
        name="container-form-type-list",
    ),
    path(
        "container-providers",
        ContainerProviderListView.as_view(),
        name="container-provider-list",
    ),
    path(
        "shipping-types",
        ShippingTypeListView.as_view(),
        name="shipping-type-list",
    ),
    path(
        "container-announcements",
        ContainerAnnouncementListView.as_view(),
        name="container-announcement-list",
    ),
]
