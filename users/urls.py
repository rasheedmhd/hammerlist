from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout"),
]
