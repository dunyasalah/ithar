from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/campaigns/', include('campaigns.urls')),
    path('api/donations/', include('donations.urls')),
    path('api/admin/', include('admin_dashboard.urls')),
]

