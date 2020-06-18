from django.contrib import admin
from .models import Empanelment,DropDown,City,State,ServiceProvider,Accredition
# Register your models here.

# class EmpanelAdmin(admin.ModelAdmin):
#     empan = ['address','department','appointmentSchedule','location','landmark','doctorName']
#     # odering = ['Name']
#     # search_fields = ['Name']
admin.site.register(State)
admin.site.register(ServiceProvider)
admin.site.register(City)
admin.site.register(Accredition)
admin.site.register(DropDown)
admin.site.register(Empanelment)
