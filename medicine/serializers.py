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
        fields = [
            'id', 'name', 'description', 'composition', 'price', 'manufacturer',
            'manufacturer_name', 'dosage_form', 'strength', 'is_prescription_required',
            'stock_quantity', 'image', 'created_by', 'created_by_username', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_by_username', 'created_at', 'updated_at']


    