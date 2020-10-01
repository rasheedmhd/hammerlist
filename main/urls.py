from django.urls import path
from .views import ( 
	home,
	ads,
	category,
	furnitures,
	furniture_detail,
)

app_name = "home"

urlpatterns = [
	path('',  home, name="home"),
	path('ads/join/', ads, name="ads"),
	path('furniture/categories/<str:slug>/', category, name="category"),
	path('furniture/', furnitures, name="furniture"),
	path('furniture/details/<int:pk>/', furniture_detail.as_view(), name="furniture_detail"),
]