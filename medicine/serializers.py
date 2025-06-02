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

class MedicineSerializer(serializers.ModelSerializer):
    manufracturer_name = serializers.CharField(source='manufacturer.name', read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['created_by', 'created_by_username', 'created_at', 'updated_at']
