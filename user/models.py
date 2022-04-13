from unicodedata import name
from django.db import models
from django import forms

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        ordering = ['name']

class User(models.Model):
    staus = models.BooleanField()
    displayname = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = forms.CharField(widget=forms.PasswordInput)
    employee = models.ForeignKey('employee.New', db_column='number',on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)

    class Meta:
        ordering = ['username']
