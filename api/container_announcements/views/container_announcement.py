from rest_framework import generics, filters

from api.core.pagination import PageNumberPagination
from apps.container_announcements.models import ContainerAnnouncement
from api.container_announcements.serializers import (
    ContainerAnnouncementSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class ContainerAnnouncementListView(generics.ListAPIView):
    queryset = ContainerAnnouncement.objects.all()
    serializer_class = ContainerAnnouncementSerializer
    pagination_class = PageNumberPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = {
        "provider": ["exact"],
        "from_city": ["exact"],
        "to_city": ["exact"],
        "container_type": ["exact"],
        "container_form_type": ["exact"],
        "shipping_type": ["exact"],
        "schedule_date_from": ["gte", "lte"],
        "schedule_date_to": ["gte", "lte"],
    }
