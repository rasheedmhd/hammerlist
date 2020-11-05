from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import Furniture, Category
from .forms import PostAdForm

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

def furniture(request):
	furniture = Furniture.objects.all()
	return render(request, 'main/furniture/index.html', { 'furniture': furniture })


class furniture_detail(DetailView):
	model =  Furniture
	context_object_name = "item" #I am using item instead of the default furniture to make it similar with the name in the for loop.
	template_name = 'main/furniture/detail.html'

def dev_desks(request):
    #A Page of Desks made specifically for tech workers/coders
    return render(request, 'main/furniture/dev_desks.html')


@login_required()
def create_ad(request):
	if request.method == "POST":
		form = PostAdForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("main:furniture")
		else:
			return redirect("main:create_ad")

	else:
		form = PostAdForm()
	return render(request, 'main/furniture/create_ad.html', {'form':form})
