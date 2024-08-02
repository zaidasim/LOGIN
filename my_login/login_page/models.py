from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    text=models.TextField(max_length=200)