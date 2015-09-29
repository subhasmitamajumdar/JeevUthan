from django.shortcuts import render
from home.forms import UserRegisterForm,PetRegisterForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render(request,'loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
    return render(request,'invalid_loggedin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def registeruser(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args={}
    args.update(csrf(request))
    args['form']=UserRegisterForm()
    return render(request,'user_register.html',args)

def register_success(request):
    return render(request,'register_success.html')

def registerpet(request):
    if request.method=='POST':
        form=PetRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registeruser')
    args={}
    args.update(csrf(request))
    args['form']=PetRegisterForm()
    return render(request,'petinfo.html',args)