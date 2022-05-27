from django.contrib import admin
from .models import Quotation
from .models import Status

# Register your models here.
admin.site.register(Quotation)
admin.site.register(Status)