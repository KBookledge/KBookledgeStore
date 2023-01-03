from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorsSerializer
from .models import Author
from books.models import Book
from .permissions import IsSuperuser


class AuthorsView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser, BasePermission]
    serializer_class = AuthorsSerializer

    def get_queryset(self):
        book_id = self.kwargs['pk']
        book_obj = get_object_or_404(Book, pk=book_id)

        authors = Author.objects.filter(book=book_obj)

        return authors

    def perform_create(self, serializer):
        book_id = self.kwargs['pk']
        book_obj = get_object_or_404(Book, pk=book_id)
        self.check_object_permissions(self.request, book_obj)

        serializer.save(book_id=book_obj.pk)
