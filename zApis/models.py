from django.db import models

# Create your models here.
class Register(models.Model):
    rId=models.AutoField(primary_key=True) 
    fName=models.CharField(max_length=100)
    sName=models.CharField(max_length=100)
    eMail=models.CharField(max_length=200)

