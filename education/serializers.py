from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Specialty, Country, University, EducationForm, EducationType, EducationLanguage


class SpecialtySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Specialty)

    class Meta:
        model = Specialty
        fields = '__all__'


class CountrySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Country)

    class Meta:
        model = Country
        fields = '__all__'


class UniversitySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=University)

    class Meta:
        model = University
        fields = '__all__'


class EducationFormSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=EducationForm)

    class Meta:
        model = EducationForm
        fields = '__all__'


class EducationTypeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=EducationType)

    class Meta:
        model = EducationType
        fields = '__all__'


class EducationLanguageSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=EducationLanguage)

    class Meta:
        model = EducationLanguage
        fields = '__all__'
