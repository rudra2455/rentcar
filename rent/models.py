from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Car(models.Model):
    carname=models.CharField(max_length=50)
    carbrand=models.CharField(max_length=50)
    carphoto=models.ImageField(upload_to='rent/images/')
    price=models.IntegerField()
    cardescription=models.CharField(max_length=1000)
    fuel=models.CharField(max_length=50)
    mileage=models.IntegerField()
    average=models.IntegerField()
    passangercapacity=models.IntegerField()

class YourOrders(models.Model):
    user_name=models.CharField(max_length=50)
    car=models.IntegerField()
    hour=models.IntegerField()
    fullname=models.CharField(max_length=50)
    phone=models.IntegerField()
    booked_date=models.DateField(auto_now_add=True)
    travel_date=models.DateField()
    fk=models.ForeignKey(Car, on_delete=models.CASCADE)
    code=models.CharField(max_length=50,null=False,default='DEFAULT_CODE')
    city=models.CharField(max_length=50,null=False,default='DEFAULT_CODE')