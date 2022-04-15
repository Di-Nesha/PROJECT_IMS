from django.contrib import admin
from user.models import Status
from user.models import User
from user.models import Role

# Register your models here.
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Role)