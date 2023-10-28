from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
    A list for user to save potential future purchases
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist item {self.product.name}"
