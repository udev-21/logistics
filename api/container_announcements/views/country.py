from rest_framework import generics
from apps.container_announcements.models import Country
from api.container_announcements.serializers.country import CountrySerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
