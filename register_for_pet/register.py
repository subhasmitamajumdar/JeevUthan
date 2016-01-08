from django import forms
from captcha.fields import CaptchaField
from .models import User,Pet


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
        fields=['pet_name','pet_type','pet_description','pet_missing_date','pet_missing_loc','pet_image']
        widgets = {
            'pet_missing_date': forms.DateInput(attrs={'type':'date'}),

        }