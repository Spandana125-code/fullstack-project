from django.contrib import admin

from shopitem_app.models import customer, product

# Register your models here.
admin.site.register(customer)
admin.site.register(product)