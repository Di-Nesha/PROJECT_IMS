from tkinter import CASCADE
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Bank(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name
        
class Supplier(models.Model):
        number = models.CharField(max_length=10)
        name = models.CharField(max_length=200)
        mobile = models.CharField(max_length=10)
        land = models.CharField(max_length=10)
        email = models.EmailField(max_length=254)
        address = models.TextField()
        cpname = models.CharField(max_length=254)
        cpnumber = models.CharField(max_length=10)
        creditlimit = MoneyField(decimal_places=2, max_digits=8)
        tobepaid = MoneyField(decimal_places=2, max_digits=8)
        remarks = models.TextField()
        regdate = models.DateField(auto_now=True)
        bhname = models.CharField(max_length=200)
        bankname = models.ForeignKey(Bank,on_delete=models.CASCADE)
        baccountno = models.PositiveIntegerField()
        bbranch = models.CharField(max_length=200)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)
        item = models.ManyToManyField('item.Item')
        
        def __str__(self):
                return self.number
