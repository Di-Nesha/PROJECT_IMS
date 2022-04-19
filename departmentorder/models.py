from tkinter import Widget
from django.db import models
from djmoney.models.fields import MoneyField
from datetimewidget.widgets import DateWidget


# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
                return self.name
        
class DepartmentOrder(models.Model):
        number = models.CharField(max_length=10)
        orderdate = DateWidget(usel10n=True)
        totalamount = MoneyField(decimal_places=2, max_digits=8)
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)
        # employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)
        department = models.ForeignKey('department.Department', db_column='employee_id',on_delete=models.CASCADE)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)

        def __str__(self):
                return self.number