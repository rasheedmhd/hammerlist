from django.shortcuts import render
from django.views.generic import DetailView

from .models import Furniture, Category

# Create your views here.
def home(request):
	return render(request, 'main/homepage.html')

def ads(request):
	return render(request, 'main/ads.html')

def category(request):
	categories = Category.objects.all()
	return render(request, 'main/furniture/category.html', { 'categories': categories })

def furnitures(request):
	furnitures = Furniture.objects.all()
	return render(request, 'main/furniture/index.html', { 'furnitures': furnitures })


class furniture_detail(DetailView):
	model =  Furniture
	context_object_name = "item" #I am using item instead of the default furniture to make it similar with the name in the for loop.
	template_name = 'main/furniture/detail.html'