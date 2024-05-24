from rest_framework import generics
from apps.logistics_services.models.services import LogisticsServiceType
from api.logistics_services.serializers.logistics_service_types import (
    LogisticsServiceTypeSerializer,
)


class LogisticsServiceTypesListView(generics.ListAPIView):
    queryset = LogisticsServiceType.objects.all()
    serializer_class = LogisticsServiceTypeSerializer
