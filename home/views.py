from django.shortcuts import render
from .models import Location,Ngo
from .forms import LocationForm
# Create your views here.
def firstpage(request):
	return render(request,'1stpage.html',{})
def location(request):
		form=LocationForm()

		loc_info=Location.objects.values('location_name')

		loc_data={
				'form':form,
				'loc_det':loc_info
			}

		return render(request,'forms.html',loc_data)
def ngo(request):
		ngo_info=Ngo.objects.all()
		content={

			"ngo_info":ngo_info
		}
		return render(request,'forms.html',content)