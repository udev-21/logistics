from django.utils.translation import activate, get_language
from rest_framework import serializers
from apps.logistics_services.models.services import LogisticsService, LogisticsServiceImage
from api.logistics_services.serializers.logistics_service_types import (
    LogisticsServiceTypeSerializer,
)
from phonenumber_field.serializerfields import PhoneNumberField


class LogisticsServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticsServiceImage
        fields = ['id', 'image']


class LogisticsServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    lan = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    service_type = LogisticsServiceTypeSerializer(many=False, read_only=True)
    phone = PhoneNumberField()
    site = serializers.CharField()
    created_at = serializers.DateTimeField()
    telegram = serializers.CharField()
    instagram = serializers.CharField()
    watsapp = serializers.CharField()
    image = serializers.ImageField()

    class Meta:
        model = LogisticsService
        fields = [
            "id",
            "lan",
            "name",
            "description",
            "service_type",
            "phone",
            "site",
            "telegram",
            "instagram",
            "watsapp",
            "image",
            "created_at",
        ]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
