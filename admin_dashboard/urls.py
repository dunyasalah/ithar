from django.urls import path
from .views import UserListView, CampaignListView, VerifyCampaignView, FlagCampaignView

urlpatterns = [
    path('users/', UserListView.as_view(), name='admin-users'),
    path('campaigns/', CampaignListView.as_view(), name='admin-campaigns'),
    path('campaigns/<int:pk>/verify/', VerifyCampaignView.as_view(), name='verify-campaign'),
    path('campaigns/<int:pk>/flag/', FlagCampaignView.as_view(), name='flag-campaign'),
]
