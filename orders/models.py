from django.db import models
import uuid


class Order(models.Model):
    STATUS_CHOICES = [
        (1, ("In process")),
        (2, ("Await payment")),
        (3, ("Completed")),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book = models.ManyToManyField("books.Book", related_name="orders")
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
    amount_price = models.DecimalField(decimal_places=2)
    amount = models.PositiveSmallIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
