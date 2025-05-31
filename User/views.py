from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, permissions
from .serializers import GroupSerializer, PermissionSerializer
from .permissions import IsAdmin, IsDoctor, IsUser, IsAdminOrDoctor, is_doctor, is_admin, is_admin_or_doctor


# Create your views here.
