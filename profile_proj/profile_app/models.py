from django.db import models

# Create your models here.
class myprofile(models.Model):
    name = models.CharField(max_length=50)
    fathername = models.CharField(max_length=40)
    mothername = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    roll_no = models.IntegerField()
    stream = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    pin_code = models.IntegerField()
    gender =models.CharField(max_length=30)
    mobile_no =models.CharField(max_length=10)
    image =models.ImageField(upload_to='media',null=True)
    description = models.CharField(max_length=400)
    
