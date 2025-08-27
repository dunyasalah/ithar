from rest_framework import serializers
from .models import Campaign, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class CampaignSerializer(serializers.ModelSerializer):
    requester = serializers.ReadOnlyField(source='requester.username')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
class Meta:
    model = Campaign
    fields = ['id', 'name', 'description', 'location', 'status', 'created_at', 'requester', 'category', 'category_id']