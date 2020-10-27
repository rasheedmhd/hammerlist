from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
]
