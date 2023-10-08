from django.contrib import admin
from .models import Product, Catergory, Country, Region

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'country',
        'region',
        'price',
        'image',
    )

    ordering = ('sku',)

class CatergoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Catergory, CatergoryAdmin)
admin.site.register(Country)
admin.site.register(Region)
