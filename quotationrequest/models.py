from tkinter import CASCADE
from django.db import models

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class QuotationRequest(models.Model):
        number = models.CharField(max_length=10)
        regdate = models.DateField(auto_now=True)
        duedate = models.DateField()
        notes = models.TextField()
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)
        supplier = models.ForeignKey('supplier.Supplier', db_column='supplier_id',on_delete=models.CASCADE)


        def __str__(self):
                return self.number
