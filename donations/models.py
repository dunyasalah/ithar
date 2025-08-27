from django.db import models
from users.models import User
from campaigns.models import Campaign


class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="donations")
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)
    def __str__(self):
        return f"Donation of {self.amount} by {self.donor.username} to {self.campaign.name}"

