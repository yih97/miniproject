<<<<<<< Updated upstream
from django.shortcuts import render, redirect, get_object_or_404
from .models import Community
from django.views.generic import ListView, DetailView
# Create your views here.

def community(request):
    return render(request, "community/community.html")

=======
from django.shortcuts import render
from .models import Post

def community_page(request):
    posts = Post.objects.all()
    return render(
        request,
        "community/community.html",
        {"posts": posts}
    )
>>>>>>> Stashed changes
