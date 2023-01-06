from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    neighborhood = models.CharField(max_length=64)
    street_address = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=9)
    complement = models.TextField(
        blank=True,
        null=True,
    )
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(
       auto_now=True
    )

