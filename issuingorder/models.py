from tkinter import CASCADE
from django.db import models
from djmoney.models.fields import MoneyField
from item.models import Item

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class IssuingOrder(models.Model):
        number = models.CharField(max_length=10)
        item = models.ManyToManyField(Item)
        totalamount = MoneyField(decimal_places=2, max_digits=8)
        discountratio = MoneyField(decimal_places=2, max_digits=8)
        netamount = MoneyField(decimal_places=2, max_digits=8)
        iodate = models.DateField(auto_now=True)
        notes = models.TextField()
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)
        departmentorder = models.ForeignKey('departmentorder.DepartmentOrder', db_column='departmentorder_id',on_delete=models.CASCADE)

        def __str__(self):
                return self.number
