from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Specialty, Country, University, EducationForm, EducationType, EducationLanguage
from .serializers import (
    SpecialtySerializer,
    CountrySerializer,
    UniversitySerializer,
    EducationFormSerializer,
    EducationTypeSerializer,
    EducationLanguageSerializer,
)

# Create your views here.

class SpecialtyFilterView(APIView):
    def get(self, request):
        university = request.query_params.get("university", None)
        country = request.query_params.get("country", None)
        edu_lang = request.query_params.get("edu_lang", None)
        edu_form = request.query_params.get("edu_form", None)
        edu_type = request.query_params.get("edu_type", None)

        if university and country and edu_lang and edu_form and edu_type:
            specialties = Specialty.objects.filter(
                university__country_id=country,
                university_id=university,
                education_language_id=edu_lang,
                education_form_id=edu_form,
                education_type_id=edu_type,
            )
            serializer = SpecialtySerializer(specialties, many=True)
            return Response({"specialties": serializer.data}, status=status.HTTP_200_OK)
        elif country and edu_lang and edu_form and edu_type:
            specialties = Specialty.objects.filter(
                university__country_id=country,
                university_id=university,
                education_language_id=edu_lang,
                education_form_id=edu_form,
            )
            university_ids = specialties.values_list("university", flat=True).distinct()
            universities = University.objects.filter(id__in=university_ids)
            serializer = UniversitySerializer(universities, many=True)
            return Response({"universities": serializer.data}, status=status.HTTP_200_OK)
        elif edu_lang and edu_form and edu_type:
            specialties = Specialty.objects.filter(
                education_language_id=edu_lang,
                education_form_id=edu_form,
                education_type_id=edu_type,
            )
            country_ids = specialties.values_list("university", flat=True).distinct()
            country = Country.objects.filter(id__in=country_ids)
            serializer = CountrySerializer(country, many=True)
            return Response({"countries": serializer.data}, status=status.HTTP_200_OK)
        elif edu_form and edu_type:
            specialties = Specialty.objects.filter(education_form_id=edu_form, education_type_id=edu_type)
            edu_lang_ids = specialties.values_list("education_language", flat=True).distinct()
            edu_lang = EducationLanguage.objects.filter(id__in=edu_lang_ids)
            serializer = EducationLanguageSerializer(edu_lang, many=True)
            return Response({"edu_lang": serializer.data}, status=status.HTTP_200_OK)
        elif edu_type:
            specialties = Specialty.objects.filter(education_type_id=edu_type)
            edu_form_ids = specialties.values_list("education_form", flat=True).distinct()
            edu_form = EducationForm.objects.filter(id__in=edu_form_ids)
            serializer = EducationFormSerializer(edu_form, many=True)
            return Response({"edu_form": serializer.data}, status=status.HTTP_200_OK)
        else:
            edu_type = EducationType.objects.all()
            serializer = EducationTypeSerializer(edu_type, many=True)
            return Response({"edu_type": serializer.data}, status=status.HTTP_200_OK)
