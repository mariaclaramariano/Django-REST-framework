from django.db import models
from uuid import uuid4
# Create your models here.
class books (models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4)
    titulo= models.CharField(max_length=255)
    autor= models.CharField(max_length=255)
    lancamento= models.IntegerField()
    estado=models.CharField(max_length=50)
    paginas= models.IntegerField()
    editora= models.CharField(max_length=255)
    criacao= models.DateField(auto_now_add=True)


    