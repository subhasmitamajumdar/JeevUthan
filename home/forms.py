from django import forms
from .models import Location,Ngo,Vet,OtherUser
from captcha.fields import CaptchaField
from localflavor.in_.forms import INStateSelect,INPhoneNumberField,INZipCodeField


class LocationForm(forms.ModelForm):
    location_name = forms.ModelChoiceField(Location.objects.all(),empty_label="Select Location",label="Choose Location")
    captcha=CaptchaField()
    class Meta:
        model=Location
        fields=['location_name']

class NgoRegisterForm(forms.ModelForm):
    captcha=CaptchaField()
    ngo_contact_no1=INPhoneNumberField()
    ngo_contact_no2=INPhoneNumberField()
    ngo_contact_no3=INPhoneNumberField()
    pincode=INZipCodeField()
    ngo_address=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Ngo
        fields=['ngo_name','ngo_email','ngo_website','ngo_contact_no1','ngo_contact_no2','ngo_contact_no3','username','password','ngo_address','state','pincode']
        widgets = {
            'password': forms.PasswordInput(),
            'state':INStateSelect(),
            }

class NgoLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    class Meta:
        widgets={
            'password':forms.PasswordInput(),
        }

class VetRegisterForm(forms.ModelForm):
    captcha=CaptchaField()
    vet_clinic_no=INPhoneNumberField()
    vet_mobile_no1=INPhoneNumberField()
    vet_mobile_no2=INPhoneNumberField()
    pincode=INZipCodeField()
    vet_address=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Vet
        fields=['vet_name','vet_email','vet_website','vet_clinic_no','vet_mobile_no1','vet_mobile_no2','username','password','vet_address','state','pincode']
        widgets = {
            'password': forms.PasswordInput(),
            'state':INStateSelect(),

            }
class VetLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    class Meta:
        widgets={
            'password':forms.PasswordInput(),
        }

class OtherUserForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=OtherUser
        fields=['first_name','last_name','email','username','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class OtherUserLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
