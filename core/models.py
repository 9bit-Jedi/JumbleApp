from django.db import models
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True) 
  # handle = models.CharField(max_length=50, unique=True) 
  bio = models.TextField(blank=True, null=True) 
  profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) 

  # followers and following fileds can be added here
  groups = models.ManyToManyField(
    'auth.Group',
    related_name='core_user_set',  
    blank=True,
    help_text='The groups this user belongs to.',
    verbose_name='groups'
  )
  user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='core_user_set', 
    blank=True,
    help_text='Specific permissions for this user.',
    verbose_name='user permissions'
  )
  
  REQUIRED_FIELDS=['email','first_name']