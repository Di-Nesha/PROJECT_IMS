from django.contrib import admin
from departmentorder.models import Status
from departmentorder.models import DepartmentOrder

# Register your models here.
admin.site.register(Status)
admin.site.register(DepartmentOrder)
