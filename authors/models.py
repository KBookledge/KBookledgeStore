from django.db import models
from uuid import uuid4

# Create your models here.


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
