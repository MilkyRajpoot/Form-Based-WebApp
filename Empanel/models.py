from django.db import models

# Create your models here.

class Empanelment(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    serviceProviderCat = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    appointmentSchedule = models.DateField() 
    otherFacility = models.CharField(max_length=255)
    isTransplant = models.BooleanField()
    isEmergencyFacility = models.BooleanField()
    isTraumaCare = models.BooleanField()
    isBurnCase = models.BooleanField()
    accre = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    landmark = models.CharField(verbose_name='Near by Landmark',max_length=255,blank=False,)
    doctorName =models.CharField(max_length=255)
    doctorPhoto = models.ImageField(upload_to='images/')
    profile = models.CharField(max_length=255)
    serviceProviderPhoto = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.department)

class DropDown(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.country)

class State(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.state)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.city)

class ServiceProvider(models.Model):
    id = models.AutoField(primary_key=True)
    serviceProviderCat = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.serviceProviderCat)

class Accredition(models.Model):
    id = models.AutoField(primary_key=True)
    accredition = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.accredition)

class AddAuthPerson(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.person)