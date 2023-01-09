from rest_framework import generics

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book, Category
from .serializers import BookSerializer, BookPostUpdateSerializer, CategorySerializer

from .utils.mixins import SerializerByMethodMixin


# Create your views here.

class BookCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Book.objects.all()

    serializer_map = {
        'GET': BookSerializer,
        'POST': BookPostUpdateSerializer,
    }

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(categorys=self.request.data['categorys'])


class BookUpdateDeleteGetView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    serializer_map = {
        'GET': BookSerializer,
        'PATCH': BookPostUpdateSerializer,
        'DELETE': BookSerializer
    }

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryUpdateDeleteGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

