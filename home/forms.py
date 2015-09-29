from django import forms
from .models import Location
from captcha.fields import CaptchaField
from register_for_pet.models import User,Pet
from .models import Ngo,Vet
class LocationForm(forms.Form):
    location_name = forms.ModelChoiceField(Location.objects.all(),empty_label="Select Location",label="Choose Location")
    captcha=CaptchaField()
    class Meta:
        model=Location
class UserRegisterForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=User
        fields=['firstname','lastname','email','contact','address','city','username','password']
        widgets = {
            'password': forms.PasswordInput(),
            }
class PetRegisterForm(forms.ModelForm):
    class Meta:
        model=Pet
        fields=['pet_name','pet_height','pet_breed','pet_colour','pet_type','pet_missing_date','pet_missing_loc']

class NgoRegisterForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Ngo
        fields=['ngo_name','ngo_email','ngo_website','ngo_contact_no1','ngo_contact_no2','ngo_contact_no3','username','password','ngo_address','ngo_location_id']
        widgets = {
            'password': forms.PasswordInput(),
            }

class VetRegisterForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Vet
        fields=['vet_name','vet_email','vet_website','vet_clinic_no','vet_mobile_no1','vet_mobile_no2','username','password','vet_address','vet_location_id']
        widgets = {
            'password': forms.PasswordInput(),
            }
