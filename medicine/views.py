from django.shortcuts import render
from django.filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Medicine, MedicineCompany
from .serializers import MedicineSerializer, MedicineCompanySerializer, MedicineCompanyAdminSerializer
from users.permissions import (IsAuthenticatedOrAdminCreate, IsAdminOrReadOnly, is_admin,
                               IsAdminOrDoctor, is_doctor)
from rest_framework.exceptions import PermissionDenied

class MedicinePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100





