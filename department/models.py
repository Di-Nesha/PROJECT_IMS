from django.db import models

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

        
class Department(models.Model):
        number = models.CharField(max_length=10)
        name = models.CharField(max_length=200)
        land = models.CharField(max_length=10)
        email = models.EmailField(max_length=254)
        fax = models.CharField(max_length=10)
        address = models.TextField()
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)

        def __str__(self):
                return self.number