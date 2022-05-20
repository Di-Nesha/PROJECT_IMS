from django.contrib import admin
from quotationrequest.models import QuotationRequest
from quotationrequest.models import Status

# Register your models here.
admin.site.register(QuotationRequest)
admin.site.register(Status)