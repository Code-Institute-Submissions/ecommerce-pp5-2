from django.contrib import admin
from .models import Product, Category, Country, Region, Promotion

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'sku',
        'category',
        'country',
        'region',
        'price',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Promotion)
