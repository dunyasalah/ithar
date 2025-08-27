from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
def __str__(self):
    return self.name
class Campaign(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return self.name