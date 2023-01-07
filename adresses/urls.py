from django.urls import path
from . import views


urlpatterns = [
    path("users/address/", views.AddressView.as_view()),
    path("users/address/<int:pk>/", views.AddressDetailView.as_view()),
]