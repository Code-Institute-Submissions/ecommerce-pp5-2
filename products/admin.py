from django.contrib import admin
from .models import Product, Catergory, Country, Region

# Register your models here.
admin.site.register(Product)
admin.site.register(Catergory)
admin.site.register(Country)
admin.site.register(Region)