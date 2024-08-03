# board/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HealthStatus, Finance, Goal

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class HealthStatusForm(forms.ModelForm):
    class Meta:
        model = HealthStatus
        fields = ['status', 'details']

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['income', 'expenses']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'description']
