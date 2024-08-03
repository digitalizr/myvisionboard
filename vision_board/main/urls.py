
from django.contrib import admin
from django.urls import path, include
from . import views
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('month/<str:month>/', views.month_view, name='month_view'),
    path('signup/', views.signup, name='signup'),  # Add this line
]