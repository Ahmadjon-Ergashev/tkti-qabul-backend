from rest_framework import serializers
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from user.models import Student, User


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def get_auth_user(self, phone, password):
        if phone and password:
            user = self.authenticate(phone=phone, password=password)
        else:
            msg = _('Must include "phone" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    @staticmethod
    def validate_auth_user_status(user):
        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = self.get_auth_user(phone, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=13,
        min_length=13,
        required=True,
    )
    passport = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    gender = serializers.ChoiceField(choices=['M', 'F'])
    passport_issue_date = serializers.DateField(required=True)
    pinfl = serializers.CharField(max_length=14, min_length=14, required=True)
    address = serializers.CharField(required=True)
    photo = serializers.ImageField(required=True)


    def validate_phone(self, phone):
        return phone # TODO validate phone
    
    def validate_passport(self, passport):
        return passport # TODO validate passport

    def get_student_data(self):
        return {
            'first_name': self.validated_data.get('first_name'),
            'middle_name': self.validated_data.get('middle_name'),
            'last_name': self.validated_data.get('last_name'),
            'birth_date': self.validated_data.get('birth_date'),
            'gender': self.validated_data.get('gender'),
            'photo': self.validated_data.get('photo'),
            'passport': self.validated_data.get('passport'),
            'passport_date_of_issue': self.validated_data.get('passport_issue_date'),
            'pinfl': self.validated_data.get('pinfl'),
            'address': self.validated_data.get('address'),
        }

    def save(self, request):
        phone = self.validated_data.get('phone')
        passport = self.validated_data.get('passport')
        user = User.objects.create_user(phone, password=passport)
        user.set_password(passport)
        user.save()

        cleaned_data = self.get_student_data()
        student = Student.objects.create(user=user, **cleaned_data)

        return student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'is_active']
        read_only_fields = ['is_active']
        extra_kwargs = {
            'phone': {'required': True},
        }


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['user']
