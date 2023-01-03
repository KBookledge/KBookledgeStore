from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("books/", views.BookCreateViewSerializer.as_view()),
    path("books/<str:pk>/", views.BookUpdateDeleteGetView.as_view())
]
