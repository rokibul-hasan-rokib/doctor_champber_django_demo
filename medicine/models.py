from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class MedicineCompany(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='medicine_companies/', blank=True, null=True)
    created_by = models.ForeignKey(get_user_model, on_delete=models.CASCADE, related_name='medicine_companies')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    composition = models.TestField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.ForeignKey(MedicineCompany, on_delete=models.CASCADE, related_name='medicines')
    dosage_form = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    is_prescription_required = models.BooleanField(default=True)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    created_by = models.ForeignKey(get_user_model, on_delete=models.CASCADE, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.strength}) - {self.dosage_form}"