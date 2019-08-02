from django.db import models

# Create your models here.
class Order(models.Model):
    description = models.CharField(max_length=255)
    price = models.IntegerField()
