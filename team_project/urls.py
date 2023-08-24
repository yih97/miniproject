from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("single_page.urls")),
    path("coffee/", include("coffee.urls")),
    path("community/", include("community.urls")),
]