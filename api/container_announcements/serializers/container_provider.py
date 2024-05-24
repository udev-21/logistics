from rest_framework import serializers

from apps.container_announcements.models import ContainerProvider
from phonenumber_field.serializerfields import PhoneNumberField


class ContainerProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    phone = PhoneNumberField()
    site = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = ContainerProvider
        fields = ["id", "name", "description", "phone", "site", "created_at"]
