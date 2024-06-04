from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AbstractNameTranslationOption(TranslationOptions):
    fields = ("name",)
    required_languages = ("en", "uz", "ru")


translator.register(Currency, AbstractNameTranslationOption)
