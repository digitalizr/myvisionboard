from django import forms
from .models import HealthStatus, Finance, Goal

class HealthStatusForm(forms.ModelForm):
    class Meta:
        model = HealthStatus
        fields = ['weight', 'side_view', 'front_view', 'back_view']

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['net_worth']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description']
