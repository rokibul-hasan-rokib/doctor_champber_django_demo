from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class MedicineCompany(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='medicine_companies/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicine_companies')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name