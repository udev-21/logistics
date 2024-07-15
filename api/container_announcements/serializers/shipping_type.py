from django.utils.translation import activate, get_language
from rest_framework import serializers

from apps.container_announcements.models import ShippingType


class ShippingTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    bg_color = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    lan = serializers.SerializerMethodField()

    class Meta:
        model = ShippingType
        fields = ["id", "lan", "name", "bg_color", "created_at"]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
