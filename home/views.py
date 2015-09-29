from django.shortcuts import render
from .models import Location,Ngo
from .forms import LocationForm,NgoRegisterForm,VetRegisterForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def firstpage(request):
	return render(request,'1stpage.html',{})

def location(request):
	form=LocationForm()
	loc_data={
			'form':form
			}
	if request.method=='POST':
		form=LocationForm(request.POST or None)
		if form.is_valid():
			l=request.POST.get('location_id')
			print l
	return render(request,'home.html',loc_data)

def ngo(request):
	form=NgoRegisterForm()
	if request.method=='POST':
		form=NgoRegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
	return render(request,'ngo_register.html',{'form':form})

def vet(request):
	form=VetRegisterForm()
	if request.method=='POST':
		form=VetRegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
	return render(request,'vet_register.html',{'form':form})
