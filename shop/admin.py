from django.contrib import admin
from parler.admin import TranslatableAdmin

from shop.models import Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'price', 'created', 'updated', 'available']
    list_editable = ['available']
    list_filter = ['created', 'available']
    raw_id_fields = ['posts']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
