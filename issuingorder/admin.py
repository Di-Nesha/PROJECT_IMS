from django.contrib import admin
from issuingorder.models import Status
from issuingorder.models import IssuingOrder

# Register your models here.
admin.site.register(Status)
admin.site.register(IssuingOrder)
