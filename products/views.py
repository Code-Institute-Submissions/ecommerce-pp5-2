from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Country, Region

# Create your views here.


def all_products(request):
    """Show all products, with sorting and search"""

    products = Product.objects.all()
    all_countries = Country.objects.all()
    all_regions = Region.objects.all()
    query = None
    categories = None
    countries = None
    regions = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)

    if request.GET:
        if 'region' in request.GET:
            regions = request.GET['region'].split(',')
            products = products.filter(region__name__in=regions)
            regions = Region.objects.filter(name__in=regions)
            

        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, 'You did not enter a serch criteria')
                    return redirect(reverse('products'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)

                products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'countries': all_countries,
        'regions': all_regions,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Show product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)



    