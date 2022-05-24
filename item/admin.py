from django.contrib import admin
from .models import Item
from .models import Status
from .models import UnitType
from .models import Category
from .models import SubCategory
from .models import Brand

# Register your models here.
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(UnitType)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)