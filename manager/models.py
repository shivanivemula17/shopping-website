from django.db import models

# Create your models here.
class addmanager(models.Model):
    FirstName=models.CharField(max_length=50,default=0)
    LastName=models.CharField(max_length=50,default=0)
    #Gender=models.Check(default=0)
    EmailAddress=models.CharField(max_length=50,default=0)
    PhoneNumber=models.IntegerField(default=0)
    Address=models.TextField(default=0)
    PostalCode=models.IntegerField(default=0)


class additem(models.Model):
    itemName=models.CharField(max_length=50,default=0)
    Description=models.CharField(max_length=100,default=0)
    cost=models.IntegerField(default=0)
    #AddPhoto=models.ImageField(default=0)
    
    
