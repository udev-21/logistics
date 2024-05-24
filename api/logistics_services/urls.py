from django.urls import path

from api.logistics_services.views.logistics_service_types import (
    LogisticsServiceTypesListView,
)

from api.logistics_services.views.logistics_services import (
    LogisticsServicesListView,
)

urlpatterns = [
    path(
        "logistics-service-types",
        LogisticsServiceTypesListView.as_view(),
        name="logistics-service-types-list",
    ),
    path(
        "logistics-services",
        LogisticsServicesListView.as_view(),
        name="logistics-services-list",
    ),
]
