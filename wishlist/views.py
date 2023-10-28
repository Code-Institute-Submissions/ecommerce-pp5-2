from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
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
        wishlist_items = Wishlist.objects.filter(user=user).all()
        messages.success(request, 'This is your wishlist')

        template = 'wishlists/wishlist.html'
        context = {
            'user': user,
            'wishlist_items': wishlist_items,
        }

        return render(request, template, context)
    else:
        messages.success(request, 'You need to be logged in to see your wish list')
        return redirect('/accounts/login')


def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            product = get_object_or_404(Product, id=product_id)
            Wishlist.objects.create(user=request.user, product=product)
            return HttpResponseRedirect(reverse('wishlist'))
    else:
        messages.success(
            request, 'You need to be logged to use the wish list')
        return redirect('/accounts/login')


def delete_from_wishlist(request, wishlist_id):
    if request.method == 'POST':
        item_to_delete = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
        item_to_delete.delete()
        messages.success(request, 'Item removed from wishlist')
        
        return HttpResponseRedirect(reverse('wishlist'))


def move_to_bag(request, item_id):
    """Add product to the bag from the wishlist"""

    product = get_object_or_404(Product, pk=item_id)

    wishlist_item = get_object_or_404(
        Wishlist, user=request.user, product=product)
    print("Wishlist item to delete: ", wishlist_item.id)
    print("Current user: ", request.user)
    try:
        wishlist_item.delete()
    except Exception as e:
        print("Error deleting item: ", e)
    
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity', 1))
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f'Added {product.name} to your bag from wishlist')

    return HttpResponseRedirect(reverse('bag'))
