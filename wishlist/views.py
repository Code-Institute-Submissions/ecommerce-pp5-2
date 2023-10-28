from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Wishlist
from products.models import Product


def wishlist(request, user, products):
    """Only for registered users"""
    if request.user.is_authenticated:
        user = request.user
        wishlist_items = Wishlist.objects.filter(user=user)
        messages.info(request, 'This is your wishlist')

        template = 'wishlist.html'
        context = {
            'user': user,
            'wishlist_items': wishlist_items,
        }

        return render(request, template, context)
    else:
        messages.info(request, 'You need to be logged in to see your wish list')

