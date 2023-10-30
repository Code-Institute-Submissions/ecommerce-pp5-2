from .models import Country, Category, Region, Promotion

"""
Allow my to use the categories across apps
"""
def country_context_processor(request):
    countries = Country.objects.all()
    return{'countries': countries}


def category_context_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}


def region_context_processor(request):
    regions = Region.objects.all()
    return {'regions': regions}


def promotion_context_processor(request):
    promotions = Promotion.objects.all()
    return {'promotions': promotions}
