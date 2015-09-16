from django.db import models

# Create your models here.

class Location(models.Model):
    location_id=models.AutoField(primary_key=True)
    location_name=models.CharField(max_length=100)
    class Meta:
        db_table='Location'
    def __str__(self):              # __unicode__ on Python 2
        return self.location_name
class Ngo(models.Model):
    ngo_id=models.AutoField(primary_key=True)
    ngo_name=models.CharField(max_length=200)
    ngo_address=models.CharField(max_length=200)
    ngo_contact_no1=models.CharField(max_length=20)
    ngo_contact_no2=models.CharField(max_length=20,blank=True)
    ngo_contact_no3=models.CharField(max_length=20,blank=True)
    ngo_location_id=models.IntegerField()
    ngo_email=models.EmailField(max_length=100,blank=True)
    ngo_website=models.URLField(max_length=100,blank=True)
    class Meta:
        db_table='Ngo'
    def __str__(self):              # __unicode__ on Python 2
        return self.ngo_name



