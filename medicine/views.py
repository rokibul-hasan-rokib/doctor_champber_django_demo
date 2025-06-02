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

class MedicineCompanyViewSet(viewsets.ModelViewSet):
    queryset = MedicineCompany.objects.all()
    serializer_class = MedicineCompanySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = MedicinePagination

    def get_serializer_class(self):
        if is_doctor(self.request.user):
            return MedicineCompanyAdminSerializer
        return MedicineCompanySerializer
    
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = MedicinePagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'description', 'strength']
    filterset_fields = ['is_prescription_required']  # Fields to filter by



