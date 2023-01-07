from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookCreateView.as_view()),
    path("books/<str:pk>/", views.BookUpdateDeleteGetView.as_view()),
    path("category/", views.CategoryCreateView.as_view()),
    path("category/<str:pk>/", views.CategoryUpdateDeleteGetView.as_view())
]
