from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import OrderSerializer
from books.models import Book
from .models import Order


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        book_obj = get_object_or_404(Book, pk=book_id)
        serializer.save(user=self.request.user, book=book_obj)


class OrderIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
