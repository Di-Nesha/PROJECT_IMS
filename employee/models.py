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
        name = models.CharField(max_length=50)

        def __str__(self):
                return self.name

        
class New(models.Model):
        number = models.CharField(max_length=10)
        fullname = models.CharField(max_length=200)
        callingname = models.CharField(max_length=75)
        photo = models.ImageField()
        nic = models.CharField(max_length=12)
        address = models.TextField()
        mobile = models.CharField(max_length=10)
        land = models.CharField(max_length=10)
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)
        gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
        civilstatus = models.ForeignKey(CiviStatus,on_delete=models.CASCADE)
        employeestatus = models.ForeignKey(Status,on_delete=models.CASCADE)
        designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
