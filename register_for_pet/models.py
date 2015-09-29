from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z][^A-Z]*$', message="name should contain only characters")
    email_regex=RegexValidator(regex=r'^[\w\.-]+@[a-z]+\.(([a-z]{2,3})|(\.([a-z]?)))\b', message="inavalid email format")
    contact_regex=RegexValidator(regex=r'[0-9]*',message="invalid contact")
    firstname=models.CharField(max_length=30,validators=[name_regex], blank=False)
    lastname=models.CharField(max_length=30,validators=[name_regex], blank=False)
    email=models.EmailField(max_length=100,validators=[email_regex], blank=False,unique=True)
    contact=models.CharField(max_length=15,validators=[contact_regex], blank=False, unique=True,null=True)
    username=models.CharField(max_length=30,blank=False,unique=True,null=True)
    password=models.CharField(max_length=30,blank=False,unique=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True)
    address=models.TextField(max_length=255,null=True)
    city=models.CharField(max_length=100,validators=[name_regex],null=True)

    def __unicode__(self):
        return str(self.username)
class Pet(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z][^A-Z]*$', message="name should contain only characters")
    height_regex=RegexValidator(regex=r'[0-9]*',message="invalid height")
    DOG='DOG'
    CAT='CAT'
    OTHER='OTHER'
    type_choice=(
        (DOG,'Dog'),
        (CAT,'Cat'),
        (OTHER,'Other'),
    )
    pet_name=models.CharField(max_length=30,validators=[name_regex], unique=False)
    pet_height=models.CharField(max_length=15,validators=[height_regex],unique=False)
    pet_colour=models.CharField(max_length=30,validators=[name_regex], unique=False)
    pet_breed=models.CharField(max_length=30,validators=[name_regex], unique=False)
    pet_missing_date=models.DateField()
    pet_missing_loc=models.CharField(max_length=30,validators=[name_regex], unique=False)
    pet_type=models.CharField(max_length=30,choices=type_choice)
    def __unicode__(self):
        return str(self.pet_name)
