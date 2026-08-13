from rest_framework.urls import path

from .views import CountryListView, EducationFormListView, EducationLanguageListView, EducationTypeListView, SpecialtyFilterView, UniversityListView

app_name = 'education'

urlpatterns = [
    path('education-form/', EducationFormListView.as_view(), name='education_form_list'),
    path('education-type/', EducationTypeListView.as_view(), name='education_type_list'),
    path('education-language/', EducationLanguageListView.as_view(), name='education_language_list'),
    path('country/', CountryListView.as_view(), name='country_list'),
    path('university/', UniversityListView.as_view(), name='university_list'),
    path('specialty/filter/', SpecialtyFilterView.as_view(), name='specialty_filter'),
]
