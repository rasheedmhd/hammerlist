from django.urls import path
from .views import ( 
	home,
	category,
	furnitures,
	furniture_detail,
)

app_name = "home"

urlpatterns = [
	path('',  home, name="home"),
	path('furnitures/categories/<str:slug>/', category, name="category"),
	path('furnitures/', furnitures, name="furnitures"),
	path('furnitures/details/<int:pk>/', furniture_detail.as_view(), name="furniture_detail"),
]