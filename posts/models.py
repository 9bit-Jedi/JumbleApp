from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.shortcuts import get_object_or_404

# Create your models here.
class Post(models.Model):
  # author : foreign key to custom user model
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=420)
  image = models.ImageField(upload_to='posts/images/')
  video = models.FileField(upload_to='posts/videos/')
  created_at = models.DateTimeField(auto_now_add=True)
  
  # def __str__(self):
  #   return f"Post by {self.author} at {self.created_at}"
