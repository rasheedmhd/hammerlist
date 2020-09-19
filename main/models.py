from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

Seller = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.name])

# Create your models here.
class Furniture(models.Model):
	category 		= models.ForeignKey(Category, on_delete=models.CASCADE)
	seller 			= models.ForeignKey(Seller, on_delete=models.CASCADE)
	price 			= models.CharField(max_length=6)
	#picture 		= models.ForeignKey(Photo, on_delete=models.CASCADE)
	about 			= models.CharField(max_length=240)
	description 	= models.TextField()
	seats 			= models.IntegerField(null=True, blank=True)
	material 		= models.CharField(max_length=100)
	specifications  = models.TextField(null=True, blank=True)
	slug 			= models.SlugField(max_length=240)
	created     	= models.DateTimeField(auto_now_add=True)
	updated     	= models.DateTimeField(auto_now=True)
