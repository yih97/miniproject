from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "coffee"

urlpatterns = [
    path("", views.category_page, name="coffee_list"),
    path("coffee_detail/", views.check_list, name="coffee_detail"),
]
