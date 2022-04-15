from django.contrib import admin
from privilege.models import Privilege
from privilege.models import Module

# Register your models here.
admin.site.register(Privilege)
admin.site.register(Module)