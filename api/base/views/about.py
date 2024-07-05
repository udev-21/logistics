from rest_framework import generics

from api.base.serializers.about import AboutCompanySerializer
from apps.base.models import AboutCompany


class AboutCompanyListView(generics.ListAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer