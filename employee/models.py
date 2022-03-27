from django.db import models

# Create your models here.
class Gender(models.Model):
        name = models.CharField(max_length=15)

class CiviStatus(models.Model):
        name = models.CharField(max_length=15)

class Status(models.Model):
        name = models.CharField(max_length=15)

class Designation(models.Model):
        name = models.CharField(max_length=15)
        
class Main(models.Model):
        number = models.IntegerField()
        fullname = models.CharField(max_length=200)
        callingname = models.CharField(max_length=75)
        photo = models.ImageField('jpeg','png')
        nic = models.IntegerField()
        address = models.TextField
        mobile = models.IntegerField()
        land = models.IntegerField()
        notes = models.TextField
        regdate = models.DateField(auto_now=True)
        gender_id = models.CharField(max_length=15)
        civilstatus_id = models.CharField(max_length=15)
        employeestatus_id = models.CharField(max_length=15)
        designation_id = models.CharField(max_length=15)
