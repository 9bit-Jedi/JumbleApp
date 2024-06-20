from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from core.models import User

from posts.views import post_list

# Create your views here.

def register(request):
  if request.method=='POST':
    form = UserRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('profile')
  else:
    form = UserRegistrationForm()
  return render(request, 'core/register.html', {"form":form})


def user_login(request):
  if request.method=='POST':
    form = UserLoginForm(request, data = request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      print(username, password)
      
      print(user)
      if user is not None:
        login(request, user)
        return redirect('post_list')
      else:
        form.add_error(None, "Invalid username or password")
    else:
      print(form.error_messages)
      return render(request, 'core/login.html', {"messages":form.error_messages, "form":form})
  else:
    form = UserLoginForm()
  return render(request, 'core/login.html', {"form":form})


@login_required
def user_logout(request):
  logout(request)
  messages.success(request, "You have been successfully logged out.")
  return render(request, 'core/logout_success.html')

@login_required
def profile(request):
  user = request.user
  return render(request, 'core/profile.html', {'user': user})


@login_required
def edit_profile(request):
  user = get_object_or_404(User, pk=request.user.id)
  # print (user.pk)
  if request.method == "POST":
    form = EditProfileForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
      form.save()
      return redirect('profile') 
  else:
    form = EditProfileForm(instance=user)
    return render(request, 'core/edit_profile.html', {"form":form})

# @login_required
# def edit_profile(request):
#   if request.method == 'POST':
#       # ... (Handle form submission and update user profile)
#   else:
#       # ... (Create the ProfileEditForm and pass it to the template)

#   return render(request, 'core/edit_profile.html')