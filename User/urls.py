

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/chamber/', include('chamber.urls')),
    path('api/medicine/', include('medicine.urls')),
    path('api/service/', include('chamberservice.urls')),
    path('api/appointments/', include('appointment.urls')),
    path('api/prescriptions/', include('prescription.urls')),
    path('api/system-menus/', include('systemmenu.urls')),
]