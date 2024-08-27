from rest_framework import serializers
from .models import Specialty, Country, University, EducationForm, EducationType, EducationLanguage


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class EducationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationForm
        fields = '__all__'


class EducationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationType
        fields = '__all__'


class EducationLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLanguage
        fields = '__all__'
