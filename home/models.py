from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Location(models.Model):

    location_id=models.AutoField(primary_key=True)
    location_name=models.CharField(max_length=100)
    class Meta:
        db_table='Location'
    def __str__(self):              # __unicode__ on Python 2
        return self.location_name


class Ngo(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z ]+$', message="name should contain only characters")
    email_regex=RegexValidator(regex=r'^[\w\.-]+@[a-z]+\.(([a-z]{2,3})|(\.([a-z]?)))\b', message="inavalid email format")
    contact_regex=RegexValidator(regex=r'\+[0-9\-()]*',message="invalid contact")
    ngo_id=models.AutoField(primary_key=True)
    ngo_name=models.CharField(max_length=200,validators=[name_regex],blank=False)
    ngo_address=models.TextField(max_length=200,unique=True)
    ngo_contact_no1=models.CharField(max_length=20,unique=True,validators=[contact_regex],blank=True)
    ngo_contact_no2=models.CharField(max_length=20,null=True,blank=True,validators=[contact_regex])
    ngo_contact_no3=models.CharField(max_length=20,blank=True,null=True,unique=False,validators=[contact_regex])
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
    contact_regex=RegexValidator(regex=r'[0-9]*',message="invalid contact")
    vet_id=models.AutoField(primary_key=True)
    vet_name=models.CharField(max_length=200)
    vet_address=models.TextField(max_length=200,unique=True)
    vet_clinic_no=models.CharField(max_length=20,blank=True)
    vet_mobile_no1=models.CharField(max_length=20,blank=True)
    vet_mobile_no2=models.CharField(max_length=20,blank=True)
    vet_location_id=models.IntegerField()
    vet_email=models.EmailField(max_length=100,unique=False,validators=[email_regex],blank=True)
    vet_website=models.URLField(max_length=100,blank=True,unique=False)
    username=models.CharField(max_length=100,unique=True,blank=False,null=True)
    password=models.CharField(max_length=30,blank=False,unique=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.vet_name



