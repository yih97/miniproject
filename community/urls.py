from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "community"

urlpatterns = [
    path("", views.community),
    path('login/', auth_views.LoginView.as_view(template_name='community/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:community_id>/', views.detail, name='detail'),
    path('create/', views.community_create, name='community_create'),
]
