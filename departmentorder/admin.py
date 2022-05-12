from django.contrib import admin
from departmentorder.models import DepartmentOrder
from departmentorder.models import Status

# Register your models here.
admin.site.register(DepartmentOrder)
admin.site.register(Status)