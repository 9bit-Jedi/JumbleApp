from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')

class UserLoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ('username', 'password')
    
class EditProfileForm(ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'profile_picture', 'bio']
    # widgets = {
    #   'title': forms.text(attrs={'class': 'input'}),
    # }