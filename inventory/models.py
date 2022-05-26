from django.db import models

# Create your models here.
class Status(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Inventory(models.Model):
        availableqty = models.IntegerField()
        notes = models.TextField()
        regdate = models.DateField(auto_now=True)
        status = models.ForeignKey(Status,on_delete=models.CASCADE)
        employee = models.ForeignKey('employee.New',on_delete=models.CASCADE)

        # def __str__(self):
        #         return self.callingname
