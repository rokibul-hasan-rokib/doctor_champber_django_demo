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
        if value == 'Admin':
            raise serializers.ValidationError("Role 'Admin' is reserved and cannot be used.")
        return value
         

    def create(self, validated_data):
        role = validated_data.pop('role','User')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        group = Group.objects.get(name=role)
        user.groups.add(group)

        return user;

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user is None or not user.check_password(attrs['password']):
            raise serializers.ValidationError("Invalid username or password")
        return attrs
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id', 'role']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['role'] = instance.groups.first().name if instance.groups.exists() else 'User'
        return representation
    
class PermissionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Permission
            fields = ['id', 'name', 'codename']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permissions_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        source='permissions',
        write_only=True
    )

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions', 'permissions_ids']
    def create(self, validated_data):
        permission_ids = validated_data.pop('permission_ids', [])
        group = Group.objects.create(**validated_data)
        group.permissions.set(permission_ids)
        return group
    
    def update(self, instance, validated_data):
        permission_ids = validated_data.pop('permission_ids', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        instance.permissions.set(permission_ids)
        return instance