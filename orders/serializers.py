from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerialzier):
    class Meta:
        model = Order
        fields = [
            "id"
            "books",
            "user",
            "amount",
            "status",
        ]

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "amount":
                instance.amount = validated_data.get("amount", instance.amount)
