from django.db import models
from django.core.validators import RegexValidator
from localflavor.in_.models import INStateField

# Create your models here.

class Location(models.Model):

    location_id=models.AutoField(primary_key=True)
    location_name=models.CharField(max_length=100,blank=False)


    def __str__(self):              # __unicode__ on Python 2
        return self.location_name


class Ngo(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z ]+$', message="name should contain only characters")
    email_regex=RegexValidator(regex=r'^[\w\.-]+@[a-z]+\.(([a-z]{2,3})|(\.([a-z]?)))\b', message="inavalid email format")
    ngo_id=models.AutoField(primary_key=True)
    pincode=models.CharField(max_length=6,unique=False,blank=False)
    ngo_name=models.CharField(max_length=200,validators=[name_regex],blank=False)
    ngo_address=models.CharField(max_length=200,unique=True)
    state =INStateField(null=False, blank=True)
    ngo_contact_no1=models.CharField(max_length=10,unique=True,blank=False,null=True)
    ngo_contact_no2=models.CharField(max_length=10,unique=False,null=True,blank=True)
    ngo_contact_no3=models.CharField(max_length=10,unique=False,blank=True,null=True)
    ngo_location_id=models.IntegerField()
    ngo_email=models.EmailField(max_length=100,unique=False,validators=[email_regex],blank=True,null=True)
    ngo_website=models.URLField(max_length=100,unique=False,blank=True,null=True)
    username=models.CharField(max_length=100,unique=True,blank=False,null=True)
    password=models.CharField(max_length=30,blank=False,unique=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.ngo_name


class Vet(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z]$', message="name should contain only characters")
    email_regex=RegexValidator(regex=r'^[\w\.-]+@[a-z]+\.(([a-z]{2,3})|(\.([a-z]?)))\b', message="inavalid email format")
    vet_id=models.AutoField(primary_key=True)
    pincode=models.CharField(max_length=6,unique=False,blank=False)
    vet_name=models.CharField(max_length=200)
    vet_address=models.CharField(max_length=200,unique=True)
    state =INStateField(null=False, blank=True)
    vet_clinic_no=models.CharField(max_length=10,blank=True,unique=False,null=True)
    vet_mobile_no1=models.CharField(max_length=10,unique=True,blank=False,null=True)
    vet_mobile_no2=models.CharField(max_length=10,unique=False,blank=True,null=True)
    vet_location_id=models.IntegerField()
    vet_email=models.EmailField(max_length=100,unique=False,validators=[email_regex],blank=True)
    vet_website=models.URLField(max_length=100,blank=True,unique=False)
    username=models.CharField(max_length=100,unique=True,blank=False,null=True)
    password=models.CharField(max_length=30,blank=False,unique=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.vet_name

class OtherUser(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z]$', message="name should contain only characters")
    email_regex=RegexValidator(regex=r'^[\w\.-]+@[a-z]+\.(([a-z]{2,3})|(\.([a-z]?)))\b', message="inavalid email format")
    first_name=models.CharField(max_length=200,blank=False,unique=False,validators=[name_regex],null=True)
    last_name=models.CharField(max_length=200,blank=False,unique=False,validators=[name_regex],null=True)
    username=models.CharField(max_length=200,blank=False,unique=True,validators=[name_regex],null=True)
    email=models.EmailField(max_length=100,validators=[email_regex], blank=False,unique=True)
    password=models.CharField(max_length=30,blank=False,unique=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.user_name


