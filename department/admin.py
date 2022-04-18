from django.contrib import admin
from department.models import Department
from department.models import Status

# Register your models here.
admin.site.register(Department)
admin.site.register(Status)
