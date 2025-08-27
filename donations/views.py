from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Donation
from .serializers import DonationSerializer
from campaigns.models import Campaign

class DonationCreateView(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        campaign_id = self.request.data.get("campaign_id")
        campaign = Campaign.objects.get(id=campaign_id)
        serializer.save(donor=self.request.user, campaign=campaign)

class DonationHistoryView(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Donation.objects.filter(donor=self.request.user)
    
class MarkDonationReceivedView(generics.UpdateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        donation = self.get_object()
        if self.request.user.role == "requester":
            serializer.save(received=True)