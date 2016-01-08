from django.shortcuts import render
from .models import Location,Ngo,OtherUser
from .forms import LocationForm,NgoRegisterForm,VetRegisterForm,OtherUserForm
from .forms import OtherUserLoginForm

# Create your views here.
def homepage(request):
	return render(request,'index.html',{})

def aboutus(request):
	return render(request,'about.html',{})

def faqs(request):
	return render(request,'faqs.html',{})

def contactus(request):
	return render(request,'contactus.html',{})

def location(request):
	form=LocationForm()
	content={
		'form':form
	}
	if request.method=='POST':
		form=LocationForm(request.POST)
		if form.is_valid():
			l=form.cleaned_data['location_name']
			loc_id=Location.objects.filter(location_name="l")
			ngo_loc_id=Ngo.objects.all()
			for nli in ngo_loc_id:
				if nli==loc_id:
					print l
	return render(request,'home.html',content)

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

def otheruser(request):
	other_user_reg_form=OtherUserForm()
	other_user_login_form=OtherUserLoginForm()
	if request.method=='POST' and 'reg' in request.POST:
		other_user_reg_form=OtherUserForm(request.POST or None)
		if other_user_reg_form.is_valid():
			other_user_reg_form.save()
	else:
		other_user_login_form=OtherUserLoginForm(request.POST or None)
		username=other_user_login_form.cleaned_data['username']
		password=other_user_login_form.cleaned_data['password']
		u = OtherUser.objects.get(username=username)
    	if u.password == password:
        	request.session['user_id'] = u.id

	return render(request,'otheruser.html',{'rform':other_user_reg_form,'lform':other_user_login_form})

