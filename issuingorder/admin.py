from django.contrib import admin
from issuingorder.models import Status, IssuingOrder, IssuingItem

# Register your models here.
admin.site.register(Status)
admin.site.register(IssuingOrder)
admin.site.register(IssuingItem)

