from rest_framework import serializers

from apps.container_announcements.models import Country


class CityListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    country_id = serializers.IntegerField(read_only=True, source="country.id")

    class Meta:
        model = "City"
        fields = ["id", "name", "created_at", "country_id"]


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    cities = CityListSerializer(many=True)

    class Meta:
        model = Country
        fields = ["id", "name", "created_at", "cities"]
