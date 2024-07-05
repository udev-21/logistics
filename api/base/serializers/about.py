from rest_framework import serializers

from apps.base.models import Currency, AboutCompany


class AboutCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutCompany
        fields = ["id", "title", "desc", "image", "phone", "telegram_link", "whatsapp_link", ]