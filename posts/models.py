from django.db import models
from core.models import User
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

from django.shortcuts import get_object_or_404

# Create your models here.
class Post(models.Model):
  # author : foreign key to custom user model
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=48)
  text = models.TextField(max_length=420)
  image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
  video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  
  def __str__(self):
    return f"Post by {self.author} : {self.title}... at {self.created_at}"


# class Comment(models.Model):
#   post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
#   author = models.ForeignKey(User, on_delete=models.CASCADE)
#   content = models.CharField(max_length=128)
#   created_at = models.DateTimeField(auto_now_add=True)
  
#   def __str__(self):
#     return f"Comment by {self.author} on {self.post}"

# class Like(models.Model):
#   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   created_at = models.DateTimeField(auto_now_add=True)
  
#   class Meta:
#     unique_together = ('post', 'user')

#   def __str__(self):
#     return f"{self.user} likes {self.post}"
