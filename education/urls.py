from rest_framework.routers import DefaultRouter

from .views import (
    CountryViewSet,
    UniversityViewSet,
    EducationFormViewSet,
    EducationTypeViewSet,
    EducationLanguageViewSet,
    SpecialtyViewSet,
)

app_name = 'education'

router = DefaultRouter()
router.register(r'country', CountryViewSet, basename='country')
router.register(r'university', UniversityViewSet, basename='university')
router.register(r'education-form', EducationFormViewSet, basename='education-form')
router.register(r'education-type', EducationTypeViewSet, basename='education-type')
router.register(r'education-language', EducationLanguageViewSet, basename='education-language')
router.register(r'specialty', SpecialtyViewSet, basename='specialty')

urlpatterns = router.urls

