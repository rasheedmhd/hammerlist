from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegistrationForm, EditUserForm


# Register your models here.
User = get_user_model() #Profile

class ProfileAdmin(UserAdmin):
	add_form = RegistrationForm
	form = EditUserForm
	model = User
	list_display = ['username', 'email',]

admin.site.register(User, ProfileAdmin)
