from django.contrib import admin

# Register your models here.

from .models import User, Student


admin.site.register(User)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'passport',
        'pinfl',
        'graduated_institution',
        'education_degree',
        'education_type',
        'education_language',
    )
    list_filter = (
        'gender',
        'education_degree',
        'education_type',
        'education_language',
    )
    search_fields = (
        'first_name',
        'last_name',
        'passport',
        'pinfl',
        'graduated_institution',
    )