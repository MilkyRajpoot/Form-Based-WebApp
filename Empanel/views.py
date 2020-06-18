from .forms import EmpanelForm,DropDownModelForm,CityModelForm,StateModelForm,AccreditionModelForm,ServiceProviderModelForm,AddAuthPersonModelForm
from .models import Empanelment,DropDown,State,City,ServiceProvider,Accredition,AddAuthPerson
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

# Show List of All Data
@login_required(login_url="/admin/")
def list_view(request):
    query = request.GET.get("qury", None)
    obj = Empanelment.objects.all().values()
    context = {"object_list" : obj}
    template = "allEmpanelList.html"    
    return render(request, template, context)

# Create a New Empanelment
@login_required(login_url="/login/")
def create(request):
    form = EmpanelForm(request.POST,request.FILES)
    template = "createEmpanel.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home/empanellist")
    else: 
        form = EmpanelForm()   
    return render(request, template, context)


# Get Infomation of Particular Empanelment According to Id 
@login_required(login_url="/login/")
def detail_view(request, id=None):
    qs = get_object_or_404(Empanelment, id=id)
    context = {"object" : qs}
    template = "getEmpanelData.html"
    return render(request, template, context)

# Can Upadate the Empanelment Data
@login_required(login_url="/login/")
def update_view(request, id=None):
    obj = get_object_or_404(Empanelment, id=id)
    template = "updateEmpanel.html"
    form = EmpanelForm(request.POST or None, instance=obj)
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/empanellist{num}".format(num=obj.id))
    return render(request, template, context)

# Add More Data into DropDown Lists 
@login_required(login_url="/login/")
def addmore(request):
    template = 'dropdownData.html'
    return render(request, template)

# Add New Country into DropDown List
def adddropdowncountry(request):
    form = DropDownModelForm(request.POST,request.FILES)
    template = "adddrop.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = DropDownModelForm()   
    return render(request, template, context)

# Add New State into DropDown List
def adddropdownstate(request):
    form = StateModelForm(request.POST,request.FILES)
    context = {"form": form}
    template = "adddrop.html"
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = StateModelForm()   
    return render(request, template, context)

# Add New City into DropDown List
def adddropdowncity(request):
    form = CityModelForm(request.POST,request.FILES)
    template = "adddrop.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = CityModelForm()   
    return render(request, template, context)

# Add New Service Provider Category into DropDown List
def adddropdownservice(request):
    form = ServiceProviderModelForm(request.POST,request.FILES)
    template = "adddrop.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = ServiceProviderModelForm()   
    return render(request, template, context)

# Add New Accredition into DropDown List
def adddropdownaccre(request):
    form = AccreditionModelForm(request.POST,request.FILES)
    template = "adddrop.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = AccreditionModelForm()   
    return render(request, template, context)

# Add New Accredition into DropDown List
def addauthperson(request):
    form = AddAuthPersonModelForm(request.POST,request.FILES)
    template = "adddrop.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home")
    else: 
        form = AddAuthPersonModelForm()   
    return render(request, template, context)