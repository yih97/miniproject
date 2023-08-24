from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "coffee"

urlpatterns = [
    # path("", views.CoffeeList.as_view(), name="coffee_list"),
    path("", views.category_page, name="coffee_list"),
    # path("<int:pk>/", views.CoffeeDetail.as_view()),
    path("coffee_detail/", views.check_list, name="coffee_detail"),
    # path("coffee_detail/", views.category_page),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)