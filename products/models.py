from django.db import models
from decimal import Decimal, ROUND_UP
from django.utils.text import slugify


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'countries'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):

    class Meta:
        verbose_name_plural = 'regions'

    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, related_name='regions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    class Meta:
        verbose_name_plural = 'Promotions'
    
    name = models.CharField(max_length=50)
    discount_percentage = models.PositiveIntegerField(null=True, blank=True, 
     help_text="Enter discount as percentage(e.g., 10 for 10 %)")
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, 
    blank=True, help_text="Enter a fixed discount amount.")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        Country, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(
        Region, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(unique=True, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='product_images/', null=True, blank=True)
    promotion = models.ForeignKey(
        Promotion, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} - {self.year} - {self.category}')
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        if self.promotion:
            if self.promotion.discount_percentage:
                discount = Decimal(self.promotion.discount_percentage) / Decimal(100)
                discounted_price = self.price * (Decimal(1) - discount)
                return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_UP) 
            elif self.promotion.discount_amount:
                return self.price - self.promotion.discount_amount
            return self.price

    def __str__(self):
        return f'{self.name} ({self.year})' if self.year else f'{self.name}'
