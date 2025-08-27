from rest_framework import generics, permissions
from users.models import User
from users.serializers import UserSerializer
from campaigns.serializers import CampaignSerializer
from campaigns.models import Campaign

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class CampaignListView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAdmin]

class VerifyCampaignView(generics.UpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAdmin]

    def perform_update(self, serializer):
        serializer.save(status="open")  

class FlagCampaignView(generics.UpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAdmin]
    def perform_update(self, serializer):
        serializer.save(status="closed")  