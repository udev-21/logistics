from django.utils.translation import activate, get_language
from rest_framework import serializers

from apps.container_announcements.models import Country


class CityListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    country_id = serializers.IntegerField(read_only=True, source="country.id")
    lan = serializers.SerializerMethodField()

    class Meta:
        model = "City"
        fields = ["id", "lan", "name", "created_at", "country_id"]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    cities = CityListSerializer(many=True)
    lan = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ["id", "lan", "name", "created_at", "cities"]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
