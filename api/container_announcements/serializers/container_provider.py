from django.utils.translation import activate, get_language
from rest_framework import serializers

from apps.container_announcements.models import ContainerProvider
from phonenumber_field.serializerfields import PhoneNumberField


class ContainerProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    phone = PhoneNumberField()
    site = serializers.CharField()
    telegram = serializers.CharField()
    instagram = serializers.CharField()
    watsapp = serializers.CharField()
    created_at = serializers.DateTimeField()
    lan = serializers.SerializerMethodField()

    class Meta:
        model = ContainerProvider
        fields = [
            "id",
            "lan",
            "name",
            "description",
            "phone",
            "site",
            "telegram",
            "instagram",
            "watsapp",
            "created_at",
        ]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
