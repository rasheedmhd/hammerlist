from django.contrib import admin

# Register your models here.
from .models import Category, Furniture, Picture

admin.site.register(Category)
admin.site.register(Furniture)
admin.site.register(Picture)

