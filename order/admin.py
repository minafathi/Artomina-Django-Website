from django.contrib import admin
from .models import Order, Kind, Size, Price

admin.site.register(Order)
admin.site.register(Kind)
admin.site.register(Size)
admin.site.register(Price)
