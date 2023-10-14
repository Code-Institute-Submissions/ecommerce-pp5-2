from django.contrib import admin
from .models import Product, Category, Country, Region, Promotion

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'year',
        'sku',
        'category',
        'country',
        'region',
        'price',
        'promotion',
        'image', 
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Promotion)
