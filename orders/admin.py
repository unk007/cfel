from django.contrib import admin

# Register your models here.

from .models import Table, Product

admin.site.register(Table)
admin.site.register(Product)