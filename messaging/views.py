from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from core.models import User

# Create your views here.

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("user_login")
    context = {}
    return render(request, "messaging/chatPage.html", context)