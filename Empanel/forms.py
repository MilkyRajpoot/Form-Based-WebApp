from django import forms  
from .models import Empanelment,DropDown,City,State,ServiceProvider,Accredition,AddAuthPerson

class EmpanelForm(forms.ModelForm):  

    person = forms.ModelChoiceField(queryset=AddAuthPerson.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(queryset=DropDown.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    state = forms.ModelChoiceField(queryset=State.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    serviceProviderCategory = forms.ModelChoiceField(queryset=ServiceProvider.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    accre = forms.ModelChoiceField(queryset=Accredition.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Empanelment
        fields = [
            'person',
            'country',
            'state',
            'city',
            'address',
            'serviceProviderCategory',
            'department',
            'appointmentSchedule',
            'otherFacility',
            'isTransplant',
            'isEmergencyFacility',
            'isTraumaCare',
            'isBurnCase',
            'accre',
            'location',
            'landmark',
            'doctorName',
            'doctorPhoto',
            'profile',
            'serviceProviderPhoto' 
            ]

        labels = {
            'address': ('Enter Complete Address'),
            'department':('Enter Department'),
            'otherFacility':("What Other Facility and Specility want ?"),
            'appointmentSchedule':('Choose Appointment Date'),
            'doctorName':('Enter Doctor Name'),
            'location':("Enter Location"),
            'landmark':("Enter Near'by Landmark"),
            'profile':('Enter Profile'),
            'isTransplant':('Whether transplants are Done ?'),
            'isEmergencyFacility':("Whether Emergency Facilities are Available ?"),
            'isTraumaCare':("Whether Trauma Care is Available ?"),
            'isBurnCase':("Whether Burn Case is admitted ?"),
            'serviceProviderPhoto':("Service Provider Picture")
        }

        widgets = {
            'address': forms.Textarea(attrs={'cols':10,'rows':5,'placeholder': 'Enter Address','class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Department'}),
            'otherFacility': forms.Textarea(attrs={'cols':10,'rows':5,'class':'form-control','placeholder': 'Want Anything Else...'}),
            'appointmentSchedule': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'doctorName': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Doctor Name'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Right Location'}),
            'landmark': forms.TextInput(attrs={'class':'form-control','placeholder': 'Any Landmark to get Location'}),
            'profile': forms.TextInput(attrs={'class':'form-control','placeholder': 'Profile'}),
        }

class StateModelForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state']

        widgets = {
            'state': forms.TextInput(attrs={'placeholder': 'Enter New State Name','class':'form-control'})
        }

class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']

        widgets = {
            'city': forms.TextInput(attrs={'placeholder': 'Enter New City Name','class':'form-control'})
        }

class DropDownModelForm(forms.ModelForm):
    class Meta:
        model = DropDown
        fields = ['country']

        widgets = {
            'country': forms.TextInput(attrs={'placeholder': 'Enter New Country Name','class':'form-control'})
        }

class AccreditionModelForm(forms.ModelForm):
    class Meta:
        model = Accredition
        fields = ['accredition']

        widgets = {
            'accredition': forms.TextInput(attrs={'placeholder': 'Enter New accredition Name','class':'form-control'})
        }

class ServiceProviderModelForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['serviceProviderCat']

        widgets = {
            'serviceProviderCat': forms.TextInput(attrs={'placeholder': 'Enter New ServiceProvider Name','class':'form-control'})
        }

class AddAuthPersonModelForm(forms.ModelForm):
    class Meta:
        model = AddAuthPerson
        fields = ['person']

        widgets = {
            'person': forms.TextInput(attrs={'placeholder': 'Enter New Person Name','class':'form-control'})
        }