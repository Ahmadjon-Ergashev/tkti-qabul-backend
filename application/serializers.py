from rest_framework import serializers

from user.serializers import StudentSerializer
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    specialty = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'student', 'specialty', 'invoice', 'description', 'is_approved', 'application_date', 'updated_at']
        read_only_fields = ['application_date', 'updated_at', 'is_approved', 'student']
