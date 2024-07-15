from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AbstractNameTranslationOption(TranslationOptions):
    fields = ("name",)
    required_languages = ("uz", "ru")


translator.register(Currency, AbstractNameTranslationOption)


class AboutCompanyNameTranslationOption(TranslationOptions):
    fields = ("title", 'desc')
    required_languages = ("uz", "ru")


translator.register(AboutCompany, AboutCompanyNameTranslationOption)
