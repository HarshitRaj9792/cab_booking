from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models as gis_models
# Create your models here.
class User(AbstractUser):
    userChoice=(
    ('Customer','Customer')
    ,('Driver','Driver')
)

    UserType= models.CharField(max_length=10,choices=userChoice,)
    email = models.EmailField(unique=True)
    Pnum = models.CharField(max_length=10, blank = True,null=True,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first name','last name','UserType']

class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, related_name='customer_pro')
    currentLocation= gis_models.PointField(blank = True,null=True,srid=4326)

class Driver(models.Model):
    Duser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='driver_profile')
    Dlicense_number = models.CharField(max_length=50, unique=True)
    Dvehicle_model = models.CharField(max_length=100)
    Dvehicle_plate_number = models.CharField(max_length=20, unique=True)
    Dvehicle_color = models.CharField(max_length=50, blank=True, null=True)
    Dcurrent_location = gis_models.PointField(null=True, blank=True, srid=4326)
    Dis_available = models.BooleanField(default=False)

class CabType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    MinFare= models.DecimalField(max_digits=8,decimal_places=2)


class Trip(models.Model):
    StatChoice =(
    ('WAITING','waiting')
    ,('BOOKED','booked'),
    ('ONGOIONG','OnGoing')
     ,('completed','completed')
    )

    customer = models.ForeignKey(Customer,on_delete=CASCADE,related_name='trips_as_Customer')
    driver=models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='trips_as_driver')

    startLocation = gis_models.PointField(srid=4326)
    endLocation = gis_models.PointField(srid=4326)

    pickupAddress = models.CharField(max_length=255)
    destAddress = models.CharField(max_length=255)

    reqCabType = models.ForeignKey(CabType, on_delete=models.SET_NULL, null=True, blank=True)

    startTime = models.DateTimeField(auto_now_add=True)
    endTime=models.DateTimeField(null=True,blank=True)

    tripRecords = models.DateTimeField(auto_now=True)

#class Meta:
 #   ordering = ['-start_time']