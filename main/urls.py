from django.urls import path
from .views import ( 
	home,
	category,
)

app_name = "home"

urlpatterns = [
	path('',  home, name="home"),
	path('furnitures/categories/<str:slug>/', category, name="category"),
]