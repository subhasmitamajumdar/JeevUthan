from django import forms
from .models import Location

class LocationForm(forms.Form):
    location_name = forms.ModelChoiceField(queryset=Location.objects.values('location_name'),empty_label="Select Location")
    def __str__(self):
        return self.location_name


