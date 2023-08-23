from rest_framework import serializers
from books import models
class booksSrerializer (serializers.ModelSerializer):
    class Meta:
        model= models.books
        fields = '__all__'
