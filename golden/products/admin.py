from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price_per_gram', 'total_price')
    search_fields = ('name',)
    list_filter = ('price_per_gram',)