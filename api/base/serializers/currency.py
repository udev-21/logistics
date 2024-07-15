from django.utils.translation import activate, get_language
from rest_framework import serializers

from apps.base.models import Currency


class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    lan = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = ["id", "lan", "name", ]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
