from django.db import models


class Paymount(models.Model):
    reference = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="purchases",
    )
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
