from tkinter import CASCADE
from django import forms
from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
        
class Privilege(models.Model):
    sel = models.BooleanField()       
    ins = models.BooleanField()        
    upd = models.BooleanField()        
    delt = models.BooleanField()        
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    role = models.ForeignKey('user.role', db_column='role_id',on_delete=models.CASCADE)

    def __str__(self):
        return self.sel
