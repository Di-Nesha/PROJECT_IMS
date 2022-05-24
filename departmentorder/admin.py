from django.contrib import admin
from departmentorder.models import DepartmentOrder, DepartmentItem, Status

# Register your models here.
admin.site.register(DepartmentOrder)
admin.site.register(Status)
admin.site.register(DepartmentItem)