from rest_framework import serializers
from .models import Medicine, MedicineCompany

class MedicineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineCompany
        fields = '__all__'

class MedicineCompanyAdminSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = MedicineCompany
        fields = '__all__'
