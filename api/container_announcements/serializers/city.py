from django.utils.translation import activate, get_language
from rest_framework import serializers
from .country import CountrySerializer


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    country = CountrySerializer(many=False, read_only=True)

    country_id = serializers.IntegerField(read_only=True, source="country.id")
    lan = serializers.SerializerMethodField()

    class Meta:
        model = "City"
        fields = ["id", "lan", "name", "country", "created_at", "country_id"]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
