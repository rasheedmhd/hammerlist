from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):

	def create_user(self, email, password=None):

		if not email:
			raise ValueError("You must input your email")

		user = self.model(
			email = self.normalize_email('email'),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None):

		user = self.create_user(
			email,
			password=password,
		)

		user.is_admin = True
		user.set_password(password)
		user.save(using=self._db)
		return user


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

	objects = CustomUserManager()

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
	