from rest_framework import generics
from apps.container_announcements.models import City
from api.container_announcements.serializers.city import CitySerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
