from rest_framework import serializers
from .models import Order
from books.models import Book


class OrderSerializer(serializers.ModelSerialzier):
    class Meta:
        model = Order
        fields = [
            "id"
            "book_id",
            "user",
            "amount",
            "amount_price",
            "status",
        ]

    def create(self, validated_data):
        book_id = validated_data["book_id"]
        book_obj = Book.objects.get(id, book_id)

        price = validated_data.pop("amount_price")
        order = Order.objects.create(**validated_data)

        if book_obj.on_sale:
            price = price * (1 - (book_obj.discount / 100))
            order.amount_price.add(price)
        else:
            order.amount_price.add(price)

        return order

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "amount":
                instance.amount = validated_data.get("amount", instance.amount)
