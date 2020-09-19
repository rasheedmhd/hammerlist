from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'main/main.html')

def category(request):
	return render(request, 'main/category.html')