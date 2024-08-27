from django.contrib import admin

from .models import Country, EducationForm, EducationLanguage, EducationType, Specialty, University
# Register your models here.

admin.site.register(Country)
admin.site.register(EducationForm)
admin.site.register(EducationLanguage)
admin.site.register(EducationType)
admin.site.register(Specialty)
admin.site.register(University)
