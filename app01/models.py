from django.db import models

# Create your models here.
class Data_01(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()


