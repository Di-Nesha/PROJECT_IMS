from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=75)
        
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class User(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    displayname = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    employee = models.ForeignKey('employee.New', db_column='employee_id',on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    regdate = models.DateField(auto_now=True)

    class Meta:
        ordering = ['username']
