from django.db import models
import uuid

# cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    price = models.IntegerField()
    page_number = models.IntegerField()
    synopsis = models.TextField()
    published_year = models.IntegerField()
    page_number = models.IntegerField()
    author = models.ForeignKey(
        "authors.Author", on_delete=models.CASCADE, related_name="books"
    )
    discount = models.IntegerField(null=True)
    picture_url = CloudinaryField('imagem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
