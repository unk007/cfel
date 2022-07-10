from django.contrib import admin

# Register your models here.
from .models import Table, Money, Currency

admin.site.register(Table)
admin.site.register(Money)
admin.site.register(Currency)