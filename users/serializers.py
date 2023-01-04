from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_superuser", "registered_at", "updated_at"]
        read_only_fields = ["registered_at", "updated_at"]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'write_only': True,
                'validators': [UniqueValidator(queryset=User.objects.all())] 
            }
        }
        

    def create(self, validated_data: dict) -> User:

        if "is_superuser" in validated_data and validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict ) -> User:
        
        for key, value in validated_data.items():

            if key == "password":
                instance.set_password( value )
            else:
                setattr( instance, key, value )

        instance.save()

        return instance

