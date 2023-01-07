from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [    
    path('promotions/', views.PromotionView.as_view()),
    path("promotions/<int:pk>/", views.PromotionDetailView.as_view()),    
]
