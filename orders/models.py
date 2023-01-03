from django.db import models
import uuid


class Order(models.Model):
    STATUS_CHOICES = [
        (1, ("In process")),
        (2, ("await payment")),
        (3, ("completed")),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    books = models.ManyToManyField("books.Book", related_name="orders")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    # purchased = models.ForeignKey(
    #     "purchases.Purchase",
    #     on_delete=models.CASCADE,
    #     related_name="orders",
    # )
    amount = models.PositiveSmallIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
