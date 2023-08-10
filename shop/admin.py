from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'updated', 'available']
    list_filter = ['created', 'available']
    raw_id_fields = ['posts']
