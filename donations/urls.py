from django.urls import path
from .views import DonationCreateView, DonationHistoryView, MarkDonationReceivedView

urlpatterns = [
    path('', DonationCreateView.as_view(), name='donate'),
    path('history/', DonationHistoryView.as_view(), name='donation-history'),
    path('<int:pk>/mark-received/', MarkDonationReceivedView.as_view(), name='mark-received'),
]

