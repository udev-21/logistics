from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AbstractNameTranslationOption(TranslationOptions):
    fields = ("name",)
    required_languages = ("en", "uz", "ru")


class ContainerProviderTranslationOption(TranslationOptions):
    fields = ("name", "description")
    required_languages = ("en", "uz", "ru")


translator.register(City, AbstractNameTranslationOption)
translator.register(Country, AbstractNameTranslationOption)
translator.register(ShippingType, AbstractNameTranslationOption)
translator.register(ContainerType, AbstractNameTranslationOption)
translator.register(ContainerFormType, AbstractNameTranslationOption)
translator.register(ContainerProvider, ContainerProviderTranslationOption)
