from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/campaigns/', include('campaigns.urls')),
    path('api/donations/', include('donations.urls')),
    path('api/admin/', include('admin_dashboard.urls')),
]

