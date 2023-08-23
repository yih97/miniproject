from django.urls import path
from . import views

urlpatterns = [
    # path("", views.CoffeeList.as_view(), name="coffee_list"),
    path("", views.category_page, name="coffee_list"),
    # path("<int:pk>/", views.CoffeeDetail.as_view()),
    path("coffee_detail/", views.check_list, name="coffee_detail"),
    # path("coffee_detail/", views.category_page),
    # path('brand_list/', views.brand_list, name='brand_list'),

]