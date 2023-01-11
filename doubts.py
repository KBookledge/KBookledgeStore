import requests
import json
import ipdb

developer_url_pagseguro = "https://sandbox.api.pagseguro.com"
production_url_pagseguro = "https://api.pagseguro.com"
client_id = "95419fe2-592e-4af5-81e6-e639b209a22e"
token = "EE0479C3F7B24E3CAC530B2CF074BA2"

#                    Criando aplicação para poder criar ações em nome do usuário
# url = "https://sandbox.api.pagseguro.com/oauth2/application"

# payload = json.dumps({
#     "name": "KBookLedgeStore",
# })
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

#     ____________________________________________________________________________________


#                                     Consultando applicação
# url = "https://sandbox.api.pagseguro.com/oauth2/application/95419fe2-592e-4af5-81e6-e639b209a22e"

# payload = {}
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json',
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#                                Solicitar autorização via SMS
# url = "https://sandbox.api.pagseguro.com/oauth2/authorize/sms"

# payload = json.dumps({
#     "email": "v06680309532441906038@sandbox.pagseguro.com.br"
# })
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json',
#     'X_CLIENT_ID': '95419fe2-592e-4af5-81e6-e639b209a22e',
#     'X_CLIENT_SECRET': '9081263e-74c5-4cdc-b117-c5fe40f0786b'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#                         Confirmar autorização SMS
# url = "https://sandbox.api.pagseguro.com/oauth2/token"

# payload = json.dumps({
#     "grant_type": "sms",
#     "email": "v06680309532441906038@sandbox.pagseguro.com.br",
#     "sms_code": 123456
# })
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json',
#     'X_CLIENT_ID': '95419fe2-592e-4af5-81e6-e639b209a22e',
#     'X_CLIENT_SECRET': '9081263e-74c5-4cdc-b117-c5fe40f0786b'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#                             Renovação de access TOKEN
# url = "https://sandbox.api.pagseguro.com/oauth2/refresh"

# payload = json.dumps({
#     "grant_type": "refresh_token",
#     "refresh_token": "1fb79dfc-5db5-46af-bfde-f2cca34755c769af6a984504b16976a6c548ef7e18e7b812-ddcd-4f35-95d0-5d5d5262833f"
# })
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json',
#     'X_CLIENT_ID': '95419fe2-592e-4af5-81e6-e639b209a22e',
#     'X_CLIENT_SECRET': '9081263e-74c5-4cdc-b117-c5fe40f0786b'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________

#                         Revogar access_token
# url = "https://sandbox.api.pagseguro.com/oauth2/revoke"

# payload = json.dumps({
#     "token_type_hint": "access_token",
#     "token": "65236dc9-8ecc-48dd-817d-76fcefeceff5dcaa1eb5404da8ade35767abb2bae4e44bee-ea98-4c24-b18b-73b5ef444ab1"
# })
# headers = {
#     'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
#     'Content-Type': 'application/json',
#     'X_CLIENT_ID': '95419fe2-592e-4af5-81e6-e639b209a22e',
#     'X_CLIENT_SECRET': '9081263e-74c5-4cdc-b117-c5fe40f0786b'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#   CRIAÇÃO DE COBRANÇA COM CARTÃO DE CRÉDITO
# url = "https://sandbox.api.pagseguro.com/charges"

# payload = json.dumps({
#     "reference_id": "ex-00001",
#     "description": "Motivo do pagamento",
#     "amount": {
#         "value": 1000,
#         "currency": "BRL"
#     },
#     "payment_method": {
#         "type": "CREDIT_CARD",
#         "installments": 1,
#         "capture": False,
#         "soft_descriptor": "My Store",
#         "card": {
#             "number": "4111111111111111",
#             "exp_month": "03",
#             "exp_year": "2026",
#             "security_code": "123",
#             "holder": {
#                 "name": "Jose da Silva"
#             }
#         }
#     },
#     "notification_urls": [
#         "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
#     ],
#     "metadata": {
#         "Exemplo": "Aceita qualquer informação",
#         "NotaFiscal": "123",
#         "idComprador": "123456"
#     }
# })
# headers = {
#     'Authorization': 'afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c',
#     'Content-Type': 'application/json',
#     'x-api-version': '4.0',
#     'x-idempotency-key': ''
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#                           CRIAÇÂO DE COBRANÇA COM BOLETO
# url = "https://sandbox.api.pagseguro.com/charges"

# payload = json.dumps({
#     "reference_id": "ex-00001",
#     "description": "Motivo do pagamento",
#     "amount": {
#         "value": 1000,
#         "currency": "BRL"
#     },
#     "payment_method": {
#         "type": "BOLETO",
#         "boleto": {
#             "due_date": "2024-12-31",
#             "instruction_lines": {
#                 "line_1": "Pagamento processado para DESC Fatura",
#                 "line_2": "Via PagSeguro"
#             },
#             "holder": {
#                 "name": "Jose da Silva",
#                 "tax_id": "22222222222",
#                 "email": "jose@email.com",
#                 "address": {
#                     "street": "Avenida Brigadeiro Faria Lima",
#                     "number": "1384",
#                     "locality": "Pinheiros",
#                     "city": "Sao Paulo",
#                     "region": "Sao Paulo",
#                     "region_code": "SP",
#                     "country": "Brasil",
#                     "postal_code": "01452002"
#                 }
#             }
#         }
#     },
#     "notification_urls": [
#         "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
#     ]
# })
# headers = {
#     'Authorization': 'afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c',
#     'Content-Type': 'application/json',
#     'x-api-version': '4.0',
#     'x-idempotency-key': ''
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________

# CRIAÇÂO DE COBRANÇA COM CARTÂO DE DEBITO !!! 3DS !!!
# url = "https://sandbox.api.pagseguro.com/charges"

# payload = json.dumps({
#     "reference_id": "ex-00001",
#     "description": "Motivo de pagamento",
#     "amount": {
#         "value": 1000,
#         "currency": "BRL"
#     },
#     "payment_method": {
#         "type": "DEBIT_CARD",
#         "card": {
#             "number": "4111111111111111",
#             "exp_month": "03",
#             "exp_year": "2026",
#             "security_code": "123",
#             "holder": {
#                 "name": "Jose da Silva"
#             }
#         },
#         "authentication_method": {
#             "type": "THREEDS",
#             "cavv": "BwABBylVaQAAAAFwllVpAAAAAAA=",
#             "xid": "BwABBylVaQAAAAFwllVpAAAAAAA=",
#             "eci": "05",
#             "version": "2.1.0",
#             "dstrans_id": "DIR_SERVER_TID"
#         }
#     },
#     "notification_urls": [
#         "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
#     ],
#     "metadata": {
#         "Exemplo": "Aceita qualquer informação",
#         "NotaFiscal": "123",
#         "idComprador": "123456"
#     }
# })
# headers = {
#     'Authorization': 'afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c',
#     'Content-Type': 'application/json',
#     'x-idempotency-key': '',
#     'x-api-version': '4.0'
# }

# response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)
#     ____________________________________________________________________________________


#                         Consultando um cobrança
# url = "https://sandbox.api.pagseguro.com/charges/CHAR_1A341014-4E70-4320-9682-A10F220EFAA8"

# payload = {}
# headers = {
#     'Authorization': 'afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c',
#     'Content-Type': 'application/json',
#     'x-api-version': '4.0'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
#     ____________________________________________________________________________________


#                       BUSCANDO UM COBRANÇA 
# url = "https://sandbox.api.pagseguro.com/charges?reference_id=EE0479C3F7B24E3CAC530B2CF074BA2"

# payload = {}
# headers = {
#     'Authorization': 'afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c',
#     'Content-Type': 'application/json',
#     'x-api-version': '4.0'
# }

# response = requests.request("GET", url, headers=headers, data=payload)
# # ipdb.set_trace()
# print(response.text)
