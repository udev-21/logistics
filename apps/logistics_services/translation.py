from modeltranslation.translator import translator, TranslationOptions
from .models.services import LogisticsService, LogisticsServiceType


class LogisticsServiceTranslationOption(TranslationOptions):
    fields = ("name", "description")
    required_languages = ("en", "uz", "ru")


translator.register(LogisticsService, LogisticsServiceTranslationOption)


class LogisticsServiceTypeTranslationOption(TranslationOptions):
    fields = ("name",)
    required_languages = ("en", "uz", "ru")


translator.register(LogisticsServiceType, LogisticsServiceTypeTranslationOption)
