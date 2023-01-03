from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class UserView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsSuperuser ]

    queryset = User.objects.all()

    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]

    queryset = User.objects.all()

    serializer_class = UserSerializer
