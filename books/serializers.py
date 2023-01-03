from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = '__all__'
            depth = 1

    def to_representation(self, instance):
        representation = super(BookSerializer, self).to_representation(instance)
        representation['picture_url'] = instance.picture_url.url
        return representation

class BookPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = '__all__'
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(BookPostUpdateSerializer, self).to_representation(instance)
        representation['picture_url'] = instance.picture_url.url
        return representation