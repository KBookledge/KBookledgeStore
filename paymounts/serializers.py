from rest_framework import serializers
from .models import Paymount
import ipdb
from orders.models import Order


class PaymountsSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    #   "amount": {
#     "value": 1000,
#     "currency": "BRL"
#   },
#   "payment_method": {
#     "type": "BOLETO",
#     "boleto": {
#       "due_date": "2024-12-31",
#       "instruction_lines": {
#         "line_1": "Pagamento processado para DESC Fatura",
#         "line_2": "Via PagSeguro"
#       },
#       "holder": {
#         "name": "Jose da Silva",
#         "tax_id": "22222222222",
#         "email": "jose@email.com",
#         "address": {
#           "street": "Avenida Brigadeiro Faria Lima",
#           "number": "1384",
#           "locality": "Pinheiros",
#           "city": "Sao Paulo",
#           "region": "Sao Paulo",
#           "region_code": "SP",
#           "country": "Brasil",
#           "postal_code": "01452002"
#         }

    class Meta:
        model = Paymount
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["reference"]

    def get_amount(self, obj):
        currency = "BRL"
        ipdb.set_trace()

    def create(self, validated_data):
        orders = Order.objects.filter(user=validated_data["reference"])
        ipdb.set_trace()
        # orders[0]
        paymount = Paymount.objects.create(**validated_data)
        return paymount
