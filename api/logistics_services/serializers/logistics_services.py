from rest_framework import serializers
from apps.logistics_services.models.services import LogisticsService
from api.logistics_services.serializers.logistics_service_types import (
    LogisticsServiceTypeSerializer,
)
from phonenumber_field.serializerfields import PhoneNumberField


class LogisticsServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    service_type = LogisticsServiceTypeSerializer(many=False, read_only=True)
    phone = PhoneNumberField()
    site = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = LogisticsService
        fields = [
            "id",
            "name",
            "description",
            "service_type",
            "phone",
            "site",
            "created_at",
        ]
