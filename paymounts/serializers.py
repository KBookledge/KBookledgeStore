from rest_framework import serializers
from django.shortcuts import get_object_or_404

from adresses.models import Address
from orders.models import Order
from users.models import User

from .models import Paymount
from .paymount_methods.billet_method import BilletMethod
import ipdb


class PaymountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paymount
        fields = "__all__"
        read_only_fields = [
            "reference",
            "status",
            "value",
            "payment_method",
            "created_at",
            "link_billet_pdf",
            "link_billet_png",
            "billet"
        ]

    def create(self, validated_data):
        url = "https://sandbox.api.pagseguro.com/charges"

        orders = Order.objects.filter(user=validated_data["reference"])
        address = get_object_or_404(Address, pk=validated_data["reference"].address_id)
        user = get_object_or_404(User, pk=validated_data["reference"].id)

        # if not address:
        #     raise HTTPException()

        BilletMethod.billet(validated_data, url, user, address, orders)

        paymount = Paymount.objects.create(**validated_data)

        return paymount
