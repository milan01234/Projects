
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    readonly_fileds=('id',)
admin.site.register(Product,ProductAdmin)


