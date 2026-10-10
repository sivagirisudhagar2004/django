from django.db import models

# Create your models here.

class Data(models.Model):

    name    = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email   = models.CharField(max_length=30)

    class Meta:
        data_table = "data"
