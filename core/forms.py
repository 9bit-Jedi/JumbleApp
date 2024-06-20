from django.forms import ModelForm
from .models import User

class UserRegistrationForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'text', 'image', 'video']
    # widgets = {
    #   'title': forms.text(attrs={'class': 'input'}),
    # }