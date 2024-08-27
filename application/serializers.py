from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'student', 'specialty', 'invoice', 'description', 'is_approved', 'application_date', 'updated_at']
        read_only_fields = ['application_date', 'updated_at', 'is_approved', 'student']
