from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path("", views.community),
]
=======
    path('community/', views.community_page, name='community'),
]
>>>>>>> Stashed changes
