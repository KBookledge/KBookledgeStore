from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

# from . import views

# from authors.views import AuthorsDetailView, AuthorsView

urlpatterns = [
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path('users/', views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),

    # path("users/authors/", AuthorsView.as_view()),
    # path("users/authors/<int:pk>/", AuthorsDetailView.as_view())
]
