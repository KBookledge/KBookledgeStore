from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Address
from .serializers import AddressSerializer
from users.models import User
from .permissions import IsSuperuser


class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [BasePermission, IsSuperuser]
    serializer_class = AddressSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Address.objects.all()
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [BasePermission, IsSuperuser]
    serializer_class = AddressSerializer

    queryset = Address.objects.all()
