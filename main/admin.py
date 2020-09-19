from django.contrib import admin

# Register your models here.
from .models import Category, Furniture

admin.site.register(Category)
admin.site.register(Furniture)