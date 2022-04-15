from django.contrib import admin
from employee.models import New
from employee.models import Gender
from employee.models import Designation
from employee.models import CiviStatus
from employee.models import Status

# Register your models here.
admin.site.register(New)
admin.site.register(Gender)
admin.site.register(Designation)
admin.site.register(CiviStatus)
admin.site.register(Status)