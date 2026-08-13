from parler_rest.serializers import TranslatableModelSerializer
from .models import Specialty, Country, University, EducationForm, EducationType, EducationLanguage


class SpecialtySerializer(TranslatableModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class CountrySerializer(TranslatableModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UniversitySerializer(TranslatableModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class EducationFormSerializer(TranslatableModelSerializer):
    class Meta:
        model = EducationForm
        fields = '__all__'


class EducationTypeSerializer(TranslatableModelSerializer):
    class Meta:
        model = EducationType
        fields = '__all__'


class EducationLanguageSerializer(TranslatableModelSerializer):
    class Meta:
        model = EducationLanguage
        fields = '__all__'
