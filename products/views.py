from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Country, Region, Promotion
from collections import defaultdict
from django.template import engines


def all_products(request):
    """Show all products, with sorting and search"""

    products = Product.objects.all()
    all_countries = Country.objects.all()
    all_regions = Region.objects.all()
    all_promotions = Promotion.objects.all()
    query = None
    categories = None
    countries = None
    regions = None
    promotions = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sorkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sorkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)

        if 'region' in request.GET:
            regions = request.GET['region'].split(',')
            products = products.filter(region__name__in=regions)
            regions = Region.objects.filter(name__in=regions)

        if 'promotion' in request.GET:
            promotions = request.GET['promotion'].split(',')
            products = products.filter(promotion__name__in=promotions)
            promotions = Promotion.objects.filter(name__in=promotions)
        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(
                        request, 'You did not enter a search criteria')
                    return redirect(reverse('products'))
                queries = Q(name__icontains=query) | \
                          Q(description__icontains=query) | \
                          Q(region__name__icontains=query) | \
                          Q(country__name__icontains=query) | \
                          Q(category__name__icontains=query)

                products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    country_regions = defaultdict(list)

    for region in Region.objects.all():
        country_name = region.country.name
        country_regions[country_name].append(region.name)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'countries': all_countries,
        'regions': all_regions,
        'promotions': all_promotions,
        'current_sorting': current_sorting,
        'country_regions': country_regions,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Show product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
