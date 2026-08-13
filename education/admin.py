from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Country, EducationForm, EducationLanguage, EducationType, Specialty, University
# Register your models here.

admin.site.register(Country, TranslatableAdmin)
admin.site.register(EducationForm, TranslatableAdmin)
admin.site.register(EducationLanguage, TranslatableAdmin)
admin.site.register(EducationType, TranslatableAdmin)
admin.site.register(Specialty, TranslatableAdmin)
admin.site.register(University, TranslatableAdmin)
