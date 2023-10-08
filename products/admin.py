from django.contrib import admin
from .models import Product, Catergory, Country, Region

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
admin.site.register(Catergory)
admin.site.register(Country)
admin.site.register(Region)
