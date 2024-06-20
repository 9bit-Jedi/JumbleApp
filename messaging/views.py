from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from core.models import User

# Create your views here.

# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("user_login")
#     context = {}
#     return render(request, "messaging/chatPage.html", context)

 
@login_required
def group_chat_page(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    
    context = {}
    return render(request, "messaging/groupChatPage.html", context)


@login_required
def private_chat_list(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    user_list = User.objects.exclude(id=request.user.id) # exclude current user from the list
    context = {'user_list': user_list}
    return render(request, "messaging/privateChatList.html", context)

@login_required
def private_chat_page(request, username):
    if not request.user.is_authenticated:
        return redirect("user_login")
    context = {}
    return render(request, "messaging/privateChatPage.html", context)