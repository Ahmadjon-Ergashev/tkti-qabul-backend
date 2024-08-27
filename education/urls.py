from rest_framework.urls import path

from .views import SpecialtyFilterView

app_name = 'education'

urlpatterns = [
    path('specialty/filter/', SpecialtyFilterView.as_view(), name='specialty_filter'),
]
