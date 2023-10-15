from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.http import HttpResponseBadRequest

# Create your views here.


def view_bag(request):
    """A view to return the bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quntity of a produict to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
