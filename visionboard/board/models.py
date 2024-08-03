# board/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class HealthStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

class Finance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)  # Ensure this is the correct field you want to add

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
