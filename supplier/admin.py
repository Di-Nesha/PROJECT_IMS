from django.contrib import admin
from supplier.models import Status
from supplier.models import Supplier
from supplier.models import Bank

# Register your models here.
admin.site.register(Status)
admin.site.register(Supplier)
admin.site.register(Bank)
