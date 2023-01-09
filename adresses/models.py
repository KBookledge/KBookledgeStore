from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    country = models.CharField(
        max_length=64,
        default='Brasil'
    )
    state = models.CharField(
        max_length=64,
        null=True
    )
    city = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    neighborhood = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    street_address = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    zip_code = models.CharField(max_length=9)
    complement = models.TextField(
        blank=True,
        null=True,
    )
    number = models.CharField(
        max_length=10,
        default="S/N"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
