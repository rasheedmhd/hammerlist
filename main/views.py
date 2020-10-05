from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Furniture, Category

# Create your views here.
def home(request):
	categories = Category.objects.all()
	return render(request, 'main/homepage.html', { 'categories': categories })

def ads(request):
	return render(request, 'main/ads.html')

def category(request):
	categories = Category.objects.all()
	return render(request, 'main/furniture/category.html', { 'categories': categories })

class AdCategory(ListView):
    model = Furniture
    template_name = 'main/furniture/ad_by_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Furniture.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(AdCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

def furnitures(request):
	furnitures = Furniture.objects.all()
	return render(request, 'main/furniture/index.html', { 'furnitures': furnitures })


class furniture_detail(DetailView):
	model =  Furniture
	context_object_name = "item" #I am using item instead of the default furniture to make it similar with the name in the for loop.
	template_name = 'main/furniture/detail.html'