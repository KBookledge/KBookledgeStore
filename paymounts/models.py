from django.db import models
import uuid


class Paymount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    reference = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="purchases",
    )

    description = models.TextField(max_length=64, null=True)
    status = models.CharField(max_length=64)
    value = models.PositiveSmallIntegerField()
    payment_method = models.CharField(max_length=64)

    created_at = models.DateTimeField()
    # updated_at = models.DateTimeField(auto_now=True)
