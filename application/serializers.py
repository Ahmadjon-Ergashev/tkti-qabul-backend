from rest_framework import serializers

from user.serializers import StudentSerializer
from .models import Application
from education.models import Specialty


class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    specialty = serializers.StringRelatedField(read_only=True)
    specialty_id = serializers.PrimaryKeyRelatedField(queryset=Specialty.objects.all(), source='specialty', write_only=True)

    class Meta:
        model = Application
        fields = ['id', 'student', 'specialty', 'invoice', 'description', 'is_approved', 'application_date', 'updated_at', 'specialty_id']
        read_only_fields = ['application_date', 'updated_at', 'is_approved', 'student']
