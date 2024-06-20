from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.core import serializers

from .models import Post
from .forms import PostForm

# Create your views here.

# def index(request):
#   return render(request, "posts.html")

def post_list(request):
  posts = Post.objects.all().order_by('-created_at')
  return render(request, 'posts/posts.html', {'posts':posts})

# @login_required
def create_post(request):
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_list')
  else:
    form = PostForm()
    return render(request, 'posts/create_post.html', {"form":form})

def edit_post(request, post_id):
  post = get_object_or_404(Post, pk=post_id, author=request.user)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect('post_list') 
  else:
    form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {"form":form})

# @login_required
def delete_post(request, post_id):
  post = get_object_or_404(Post, pk=post_id, author=request.user)
  if request.method == "POST":
    post.delete()
    return redirect('post_list') 
  else:
    form = PostForm(instance=post)
    return render(request, 'posts/confirm_delete_post.html', {"post":post})
