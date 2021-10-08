from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
# Register your models here.
admin.site.register(CustomersProfile)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Orders)
admin.site.register(OrderTracking)
