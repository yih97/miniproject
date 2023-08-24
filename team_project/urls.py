from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from community import views
from team_project.settings import MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("single_page.urls")),
    path("coffee/", include("coffee.urls")),
    path("community/", include("community.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


