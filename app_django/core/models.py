from django.db import models

# Create your models here.

class Pessoas(models.Model):
    name = models.CharField(max_length=200)
    idade = models.IntegerField()