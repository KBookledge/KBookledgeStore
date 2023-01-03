from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/authors", views.AuthorsSerializer),
    path("users/authors/<str:pk>/", views.AuthorsDetailView)
]
