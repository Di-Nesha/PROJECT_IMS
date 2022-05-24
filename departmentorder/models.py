from django .db import models
from djmoney.models.fields import MoneyField
from item.models import Item

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
                return self.name
        
class DepartmentOrder(models.Model):
        number = models.CharField(max_length=10)
        # orderdate = DateWidget(usel10n=True)
        totalamount = MoneyField(decimal_places=2, max_digits=8)
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)
        department = models.ForeignKey('department.Department', db_column='employee_id',on_delete=models.CASCADE)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        item = models.ManyToManyField('item.Item', through='DepartmentItem')

        def __str__(self):
                return self.number

#ManyToMany Table - with additional attributes -  (IssuingOrder - Item)
class DepartmentItem(models.Model):
        departmentorder = models.ForeignKey(DepartmentOrder, on_delete=models.CASCADE)
        item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
        qty = models.IntegerField()
        salesprice = MoneyField(decimal_places=2, max_digits=10)
        linetotal = MoneyField(decimal_places=2, max_digits=10)

        #block - duplicate values
        class Meta:
                unique_together = [['item' , 'departmentorder']]