from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Country(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    def __str__(self):
        return self.name


class University(TranslatableModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )

    def __str__(self):
        return self.name


class EducationForm(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    def __str__(self):
        return self.name


class EducationType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    def __str__(self):
        return self.name


class EducationLanguage(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    def __str__(self):
        return self.name


class Specialty(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    education_form = models.ForeignKey(EducationForm, on_delete=models.CASCADE)
    education_type = models.ForeignKey(EducationType, on_delete=models.CASCADE)
    education_language = models.ForeignKey(EducationLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
