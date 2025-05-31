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

    def __init__(self, *args, **kwargs):
        super(UserRegistrationSerializer,self).__init__(*args, **kwargs)
        group_choices = [(group.name, group.name.capitalize()) for group in Group.objects.all()]
        self.fields['role'].choices = group_choices

    def validation_role(self, value):
        role = validated_date.pop('role','User')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        group = Group.objects.get(name=value)
        user.groups.add(group)

        return user;

