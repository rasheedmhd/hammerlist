from django.contrib.auth.models import AbstractBaseUser 
from django.db import models

# Create your models here.
class CustomUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name="Email Address",
		unique=True,
	)

	username 		= models.CharField(max_length=255)
	business_name 	= models.CharField(max_length=255)
	first_name 		= models.CharField(max_length=255)
	last_name 		= models.CharField(max_length=255)

	is_active 		= models.BooleanField(default=True)
	is_admin 		= models.BooleanField(default=False)

	USERNAME_FIELD 	= 'email'

	def _str_(self):
		return self.business_name

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin
	