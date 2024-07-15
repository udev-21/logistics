from django.utils.translation import activate, get_language
from rest_framework import serializers
from apps.logistics_services.models.services import LogisticsServiceType


class LogisticsServiceTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    lan = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    class Meta:
        model = LogisticsServiceType
        fields = ["id", "lan", "name", "created_at"]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
