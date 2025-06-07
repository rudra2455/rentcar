from django.db import models

# Create your models here.

class City(models.Model):
    city=models.CharField(max_length=100)
    
    
class Contacts(models.Model):
    fullname=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    phoneno=models.CharField(max_length=50, null=True, blank=True)
    message=models.CharField(max_length=1000, null=True, blank=True)