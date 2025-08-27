from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    donor = serializers.ReadOnlyField(source='donor.username')
    campaign = serializers.ReadOnlyField(source='campaign.name')

    class Meta:
        model = Donation
        fields = ['id', 'donor', 'campaign', 'amount', 'created_at', 'received']
