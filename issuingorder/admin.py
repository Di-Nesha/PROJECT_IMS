from django.contrib import admin
from issuingorder.models import Status, IssuingOrder, Enrollment

# Register your models here.
admin.site.register(Status)
admin.site.register(IssuingOrder)
admin.site.register(Enrollment)

