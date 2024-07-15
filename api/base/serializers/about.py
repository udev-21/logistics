from rest_framework import serializers

from apps.base.models import Currency, AboutCompany
from django.utils.translation import get_language, activate


class AboutCompanySerializer(serializers.ModelSerializer):
    lan = serializers.SerializerMethodField()

    class Meta:
        model = AboutCompany
        fields = ["id", "lan", "title", "desc", "image", "phone", "telegram_link", "whatsapp_link", ]

    def get_lan(self, obj):
        lan = self.context['request'].META.get('HTTP_LANG')
        try:
            activate(lan)
        except:
            pass
        return get_language()
