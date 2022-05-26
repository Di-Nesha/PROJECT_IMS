from django.contrib import admin
from .models import Inventory, Status

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Status)