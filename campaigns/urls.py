from django.urls import path
from .views import CampaignListCreateView, CampaignDetailView, CategoryListView

urlpatterns = [
    path('', CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
