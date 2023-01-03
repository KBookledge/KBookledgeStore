from rest_framework import generics

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer, BookPostUpdateSerializer

from .utils.mixins import SerializerByMethodMixin

# Create your views here.
class BookCreateViewSerializer(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Book.objects.all()

    serializer_map = {
        'GET': BookSerializer,
        'POST': BookPostUpdateSerializer,
    }

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
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

