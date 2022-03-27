from tkinter import CASCADE
from django.db import models

# Create your models here.
class Gender(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class CiviStatus(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Designation(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

        
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
        gender_id = models.ForeignKey(Gender,on_delete=models.CASCADE)
        civilstatus_id = models.ForeignKey(CiviStatus,on_delete=models.CASCADE)
        employeestatus_id = models.ForeignKey(Status,on_delete=models.CASCADE)
        designation_id = models.ForeignKey(Designation,on_delete=models.CASCADE)
