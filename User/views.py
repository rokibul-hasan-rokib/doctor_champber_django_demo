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
from rest_framework.decorators import action

# Create your views here.

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class LoginUser(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)   

        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'username': user.username
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserViewSet(APIView):
    def post(self, request):
        refresh = request.data.get('refresh')
        if refresh:
            try:
                refresh_token = RefreshToken(refresh)
                return Response({
                    'refresh': str(refresh_token),
                    'access': str(refresh_token.access_token),
                    'user_id': refresh_token['user_id'],
                    'username': refresh_token['username']
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)                         
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
def UserProfileUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self,request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "This is an admin-only view"}, status=status.HTTP_200_OK)
    
    