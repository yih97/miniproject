from django.urls import path
from . import views

urlpatterns = [
    path("", views.CoffeeList.as_view()),
    path("<int:pk>/", views.CoffeeDetail.as_view()),

]