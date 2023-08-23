from rest_framework import viewsets
from books.api import serializers
from books import models
 

class bookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.booksSrerializer
    queryset= models.books.objects.all()