from rest_framework import serializers
from .country import CountrySerializer


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    country = CountrySerializer(many=False, read_only=True)

    country_id = serializers.IntegerField(read_only=True, source="country.id")

    class Meta:
        model = "City"
        fields = ["id", "name", "country", "created_at", "country_id"]
