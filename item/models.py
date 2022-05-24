from pyexpat import model
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class UnitType(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Brand(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Category(models.Model):
        name = models.CharField(max_length=15)
        brand = models.ManyToManyField(Brand)

        def __str__(self):
                return self.name

class SubCategory(models.Model):
        name = models.CharField(max_length=15)
        category = models.ForeignKey(Category,on_delete=models.CASCADE)

        def __str__(self):
                return self.name

        
class Item(models.Model):
        number = models.CharField(max_length=10)
        name = models.CharField(max_length=200)
        size = models.CharField(max_length=3)
        rop = models.CharField(max_length=10)
        roq = models.CharField(max_length=10)
        qty = models.CharField(max_length=10)
        unitprice = MoneyField(decimal_places=2, max_digits=10)
        photo = models.ImageField()
        remarks = models.TextField()
        regdate = models.DateField(auto_now=True)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        unittype = models.ForeignKey(UnitType,on_delete=models.CASCADE)
        brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
        subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
        category = models.ForeignKey(Category,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)

        def __str__(self):
                return self.number
