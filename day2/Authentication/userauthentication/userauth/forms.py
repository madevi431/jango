from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UsersignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','password1','password2','email','first_name','last_name']
