from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'text', 'image', 'video']
    # widgets = {
    #   'title': forms.text(attrs={'class': 'input'}),
    # }