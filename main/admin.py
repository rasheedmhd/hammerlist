from django.contrib import admin

# Register your models here.
from .models import Category, Furniture, Picture



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class FurnitureAdmin(admin.ModelAdmin):
	list_display = [ 'category', 'seller', 'about', 'price', 'material']
	list_filter = ['created', 'price', 'material', 'updated']
	list_editable = ['about', 'price', 'about']
	prepopulated_fields = {'slug':('about',)}
	searchable_fields = ('about', 'price', 'seats', 'material')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Picture)