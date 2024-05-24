from rest_framework import serializers
from apps.logistics_services.models.services import LogisticsServiceType


class LogisticsServiceTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    class Meta:
        model = LogisticsServiceType
        fields = ["id", "name", "created_at"]
