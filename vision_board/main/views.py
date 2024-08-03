from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import MonthlyData
from .forms import MonthlyDataForm
from django.contrib.auth import login  # Add this import
from datetime import datetime

def home(request):
    return render(request, 'main/home.html')
@login_required
def dashboard(request):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthly_data = MonthlyData.objects.filter(user=request.user)
    month_order = {month: index for index, month in enumerate(months)}
    sorted_monthly_data = sorted(monthly_data, key=lambda x: month_order[x.month], reverse=True)
    return render(request, 'main/dashboard.html', {'username': request.user.username, 'months': months, 'monthly_data': sorted_monthly_data})

@login_required
def month_view(request, month):
    monthly_data, created = MonthlyData.objects.get_or_create(
        user=request.user, 
        month=month, 
        defaults={'current_weight': 0.0, 'net_worth': 0.0}
    )
    if request.method == 'POST':
        form = MonthlyDataForm(request.POST, instance=monthly_data)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MonthlyDataForm(instance=monthly_data)
    
    # Fetch and sort monthly data in descending order by month
    all_monthly_data = MonthlyData.objects.filter(user=request.user)
    month_order = {month: index for index, month in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])}
    all_monthly_data = sorted(all_monthly_data, key=lambda x: month_order[x.month], reverse=True)
    
    return render(request, 'main/month_view.html', {'form': form, 'month': month, 'all_monthly_data': all_monthly_data})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

