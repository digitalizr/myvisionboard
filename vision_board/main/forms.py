from django import forms
from .models import MonthlyData

class MonthlyDataForm(forms.ModelForm):
    class Meta:
        model = MonthlyData
        fields = ['net_worth', 'current_weight', 'month_goals']