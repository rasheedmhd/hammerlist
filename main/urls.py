from django.urls import path
from .views import (
	home,
	ads,
	category,
	furniture,
	furniture_detail,
	AdCategory,
	dev_desks,
	create_ad,
)

app_name = "main"

urlpatterns = [
	path('',  home, name="home"),
	path('ads/join/', ads, name="ads"),
	path('furniture/categories/', category, name="category"),
	path('furniture/categories/<str:slug>/', AdCategory.as_view(), name="ad_by_category"),
	path('furniture/', furniture, name="furniture"),
	path('furniture/details/<int:pk>/', furniture_detail.as_view(), name="furniture_detail"),

	path('furniture/developers', dev_desks, name="dev_desks"),
	path('furniture/create', create_ad, name="create_ad"),
]
