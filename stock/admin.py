from django.contrib import admin
from .models import Category,Firm,Brand,Product,Purchases,Sales

# Register your models here.
admin.site.register(Category)
admin.site.register(Firm)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Purchases)
admin.site.register(Sales)
