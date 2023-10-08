from django.db import models


class Catergory(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, related_name='regions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Catergory, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
