from rest_framework import serializers

from apps.base.models import Currency


class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Currency
        fields = ["id", "name", ]
