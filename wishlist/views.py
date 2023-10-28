from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Wishlist
from products.models import Product


def wishlist(request):
    """Only for registered users"""
    if request.user.is_authenticated:
        user = request.user
        wishlist_items = Wishlist.objects.filter(user=user)
        messages.success(request, 'This is your wishlist')

        template = 'wishlists/wishlist.html'
        context = {
            'user': user,
            'wishlist_items': wishlist_items,
        }

        return render(request, template, context)
    else:
        messages.success(request, 'You need to be logged in to see your wish list')
        return HttpResponseRedirect(reverse('login'))


def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        Wishlist.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(reverse('wishlist'))


def delete_from_wishlist(request, wishlist_id):
    if request.method == 'POST':
        item_to_delete = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
        item_to_delete.delete()
        messages.success(request, 'Item removed from wishlist')
        print(messages.success)
        return HttpResponseRedirect(reverse('wishlist'))


