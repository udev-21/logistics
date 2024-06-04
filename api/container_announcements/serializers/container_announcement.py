from rest_framework import serializers

from apps.container_announcements.models import ContainerAnnouncement
from api.container_announcements.serializers import *


class ContainerAnnouncementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    provider = ContainerProviderSerializer(many=False, read_only=True)
    schedule_date_from = serializers.DateTimeField()
    schedule_date_to = serializers.DateTimeField()
    from_city = CitySerializer(many=False, read_only=True)
    to_city = CitySerializer(many=False, read_only=True)
    container_type = ContainerTypeSerializer(many=False, read_only=True)
    container_form_type = ContainerFormTypeSerializer(many=False, read_only=True)
    shipping_type = ShippingTypeSerializer(many=False)
    created_at = serializers.DateTimeField()

    class Meta:
        model = ContainerAnnouncement
        fields = [
            "id",
            "provider",
            "schedule_date_from",
            "schedule_date_to",
            "price",
            "currency",
            "is_by_agreement",
            "from_city",
            "to_city",
            "container_type",
            "container_form_type",
            "shipping_type",
            "created_at",
        ]
