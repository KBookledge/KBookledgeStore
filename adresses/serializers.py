from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from .models import Address
import requests


class AddressSerializer(serializers.ModelSerializer):
    zip_code = serializers.CharField(
        error_messages={"Max-length": "Data should be 9 digits"},
    )

    class Meta:
        model: Address
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "complement": {"allow_null": True},
            "number": {"allow_null": True},
        }

    def create_address_from_cep(self, validated_data: dict) -> Address:

        cep = (
            validated_data["zipcode"].replace("-", "").replace(".", "").replace(" ", "")
        )
        if len(cep) == 8:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

            dict_address = JSONParser().parse(response)

            address = Address(
                country=validated_data["country"],
                state=validated_data["state"],
                city=dict_address["localidade"],
                neighborhood=dict_address["bairro"],
                street_address=dict_address["logradouro"],
                complement=dict_address["complemento"],
                number=validated_data["complemento"],
                zip_code=validated_data["zip_code"],
            )

            return address

    def update_address(self, instance: Address, validated_data: dict) -> Address:
        for key, value in validated_data.items():

            setattr(instance, key, value)

        instance.save()

        return instance
