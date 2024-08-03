from django.db import models
from django.contrib.auth.models import User

class MonthlyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    net_worth = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    month_goals = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.month}"