from django.db import models
from .forms import *

# Create your models here.

class MyfileUpload(models.Model):

    my_file = models.FileField()