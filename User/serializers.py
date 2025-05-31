from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(choices=[],write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']