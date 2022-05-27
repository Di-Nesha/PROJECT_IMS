from tkinter import CASCADE
from django.db import models

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name
        
class Quotation(models.Model):
        number = models.CharField(max_length=10)
        validatefrom = models.DateField()
        validateto = models.DateField()
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        quotationrequest = models.ForeignKey('quotationrequest.QuotationRequest',on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New',on_delete=models.CASCADE)
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)

        def __str__(self):
                return self.number
