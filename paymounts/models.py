from django.db import models
import uuid


class Paymount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    reference = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="paymounts",
    )
    billet = models.OneToOneField(
        "billets.Billet", on_delete=models.CASCADE, related_name="paymount"
    )

    description = models.TextField(max_length=64, null=True)
    status = models.CharField(max_length=64)
    value = models.PositiveSmallIntegerField()
    payment_method = models.CharField(max_length=64)
    created_at = models.DateTimeField()

    link_billet_pdf = models.TextField()
    link_billet_png = models.TextField()
    # updated_at = models.DateTimeField(auto_now=True)
