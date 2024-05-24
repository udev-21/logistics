from rest_framework import generics
from apps.logistics_services.models.services import LogisticsService
from api.logistics_services.serializers.logistics_services import (
    LogisticsServiceSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class LogisticsServicesListView(generics.ListAPIView):
    queryset = LogisticsService.objects.all()
    serializer_class = LogisticsServiceSerializer

    filter_backends = (DjangoFilterBackend,)

    filterset_fields = {
        "service_type": ["exact"],
        "phone": [
            "icontains",
        ],
        "site": [
            "icontains",
        ],
        "name": [
            "icontains",
        ],
    }
