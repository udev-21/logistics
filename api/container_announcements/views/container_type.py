from rest_framework import generics
from apps.container_announcements.models import ContainerType
from api.container_announcements.serializers.container_type import (
    ContainerTypeSerializer,
)


class ContainerTypeListView(generics.ListAPIView):
    queryset = ContainerType.objects.all()
    serializer_class = ContainerTypeSerializer
