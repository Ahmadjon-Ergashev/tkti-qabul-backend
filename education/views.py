from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Specialty, Country, University, EducationForm, EducationType, EducationLanguage
from .serializers import (
    SpecialtySerializer,
    CountrySerializer,
    UniversitySerializer,
    EducationFormSerializer,
    EducationTypeSerializer,
    EducationLanguageSerializer,
)


class BaseEducationViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class CountryViewSet(BaseEducationViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class UniversityViewSet(BaseEducationViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get("country", None)
        if country:
            queryset = queryset.filter(country_id=country)
        return queryset


class EducationFormViewSet(BaseEducationViewSet):
    queryset = EducationForm.objects.all()
    serializer_class = EducationFormSerializer


class EducationTypeViewSet(BaseEducationViewSet):
    queryset = EducationType.objects.all()
    serializer_class = EducationTypeSerializer


class EducationLanguageViewSet(BaseEducationViewSet):
    queryset = EducationLanguage.objects.all()
    serializer_class = EducationLanguageSerializer


class SpecialtyViewSet(BaseEducationViewSet):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        university = self.request.query_params.get("university", None)
        edu_lang = self.request.query_params.get("edu_lang", None)
        edu_form = self.request.query_params.get("edu_form", None)
        edu_type = self.request.query_params.get("edu_type", None)

        filter_kwargs = {}
        if university:
            filter_kwargs["university_id"] = university
        if edu_lang:
            filter_kwargs["education_language_id"] = edu_lang
        if edu_form:
            filter_kwargs["education_form_id"] = edu_form
        if edu_type:
            filter_kwargs["education_type_id"] = edu_type

        if filter_kwargs:
            queryset = queryset.filter(**filter_kwargs)
        return queryset

