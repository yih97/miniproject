from django.contrib.auth.decorators import login_required  # 커뮤니티 글 수정시 로그인한 상태여야 함을 구현하고자 import
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login      # 로그인 기능을 구현하기 위해 import
from community.forms import UserForm, CommunityForm
from django.contrib import messages    # 로그인한 사용자와 수정하려는 글쓴이가 다르면 '수정권한이 없습니다'라는 오류가 발생하도록 하기 위해 import
from django.utils import timezone      # timezone.now()를 사용하기 위해 import
from .models import Community
from .forms import CommunityForm

def community(request):
    community = Community.objects.all()
    return render(request,"community/community.html", {"community" : community})
  
def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    return render(request, "community/community_detail.html", {"community" : community})

def community(request):
    community = Community.objects.all()
    return render(request,"community/community.html", {"community" : community})

def community_detail(request, pk):   # 커뮤니티 글의 상세페이지를 보여주는 함수
    community = get_object_or_404(Community, pk=pk)
    return render(request, "community/community_detail.html", {"community": community})


def new(request):
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.save()
            return redirect("/community/")

    else:
        form = CommunityForm()
        return render(request, "community/new.html", {"form": form})

def update(request, pk):
    community = get_object_or_404(Community, pk=pk)

    if request.method == "POST":
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            community = form.save(commit=False)
            community.save()
            return redirect("/community/")
    else:
        form = CommunityForm(instance=community)

        return render(request, "community/new.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'community/signup.html', {'form' : form})




@login_required(login_url='community:login')
def modify(request, community_id):
    post = get_object_or_404(Community, pk=community_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('/')

    
    if request.method == "POST":
         form = CommunityForm(request.POST, instance=community)
         if form.is_valid():
             community = form.save(commit=False)
             community.author = request.user
             community.modify_date=timezone.now()
             community.save()
             return redirect("/")
         else:
             form = CommunityForm(instance=community)
         context = {'community':community, 'form': form}
         return render(request, 'community/community_form.html', context)


def delete(request, pk):  # 매개변수 설정
    community = get_object_or_404(Community, pk=pk)
    community.delete()
    return redirect("/community/")