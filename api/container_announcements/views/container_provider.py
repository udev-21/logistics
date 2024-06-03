from rest_framework import generics, pagination
from apps.container_announcements.models import ContainerProvider
from api.container_announcements.serializers.container_provider import (
    ContainerProviderSerializer,
)


class ContainerProviderListView(generics.ListAPIView):
    queryset = ContainerProvider.objects.all()
    serializer_class = ContainerProviderSerializer
    pagination_class = pagination.LimitOffsetPagination
