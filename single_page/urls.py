from django.urls import path
from . import views

app_name = "single_page"

urlpatterns = [
    path("", views.landing),
]