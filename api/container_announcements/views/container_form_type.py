from rest_framework import generics
from apps.container_announcements.models import ContainerFormType
from api.container_announcements.serializers.container_form_type import (
    ContainerFormTypeSerializer,
)


class ContainerFormTypeListView(generics.ListAPIView):
    queryset = ContainerFormType.objects.all()
    serializer_class = ContainerFormTypeSerializer
