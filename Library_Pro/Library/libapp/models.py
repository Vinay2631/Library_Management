from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=100)
    published=models.IntegerField()
    available=models.IntegerField()

