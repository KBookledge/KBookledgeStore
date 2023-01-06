from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Promotion

class PromotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ["id", "name", "starts_at", "ends_at", "updated_at", "book"]
        read_only_fields = ["created_at"]
        extra_kwargs = {
            'validators': [UniqueValidator(queryset=Promotion.objects.all())] 
        }
        
        

    def create(self, validated_data: dict) -> Promotion:

        return Promotion.objects.create_promotion(**validated_data)

    def update(self, instance: Promotion, validated_data: dict ) -> Promotion:
        
        for key, value in validated_data.items():
            setattr( instance, key, value )

        instance.save()

        return instance

