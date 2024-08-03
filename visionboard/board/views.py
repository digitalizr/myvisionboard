from django.shortcuts import render, redirect
from .forms import HealthStatusForm, FinanceForm, GoalForm
from .models import HealthStatus, Finance, Goal

def index(request):
    health_form = HealthStatusForm(request.POST or None, request.FILES or None)
    finance_form = FinanceForm(request.POST or None)
    goal_form = GoalForm(request.POST or None)

    if request.method == 'POST':
        if 'health_submit' in request.POST and health_form.is_valid():
            health_form.save()
        elif 'finance_submit' in request.POST and finance_form.is_valid():
            finance_form.save()
        elif 'goal_submit' in request.POST and goal_form.is_valid():
            goal_form.save()
        return redirect('index')

    health_status = HealthStatus.objects.last()
    finance = Finance.objects.last()
    goals = Goal.objects.all()

    context = {
        'health_form': health_form,
        'finance_form': finance_form,
        'goal_form': goal_form,
        'health_status': health_status,
        'finance': finance,
        'goals': goals,
    }
    return render(request, 'board/index.html', context)
