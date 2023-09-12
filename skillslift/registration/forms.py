from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm): #created a form inheriting from UserCreationForm 
	class Meta:
		model = User #inheriting from the default model User
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]