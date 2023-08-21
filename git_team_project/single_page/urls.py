from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing),
    path("category/<str:pk>/", views.category_page),
]