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
        item = models.ManyToManyField('item.Item', through='Enrollment')

        def __str__(self):
                return self.number

class Enrollment(models.Model):
        issuingorder = models.ForeignKey(IssuingOrder, on_delete=models.CASCADE)
        item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
        qty = models.IntegerField()
        salesprice = MoneyField(decimal_places=2, max_digits=10)
        linetotal = MoneyField(decimal_places=2, max_digits=10)

        class Meta:
                unique_together = [['item' , 'issuingorder']]