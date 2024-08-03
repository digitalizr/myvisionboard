from django.db import models

class HealthStatus(models.Model):
    weight = models.FloatField()
    side_view = models.ImageField(upload_to='images/')
    front_view = models.ImageField(upload_to='images/')
    back_view = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

class Finance(models.Model):
    net_worth = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
