from rest_framework import generics
from apps.container_announcements.models import ShippingType
from api.container_announcements.serializers.shipping_type import (
    ShippingTypeSerializer,
)


class ShippingTypeListView(generics.ListAPIView):
    queryset = ShippingType.objects.all()
    serializer_class = ShippingTypeSerializer
