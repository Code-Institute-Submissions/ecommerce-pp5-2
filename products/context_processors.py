from .models import Country, Category

def country_context_processor(request):
    countries = Country.objects.all()
    return{'countries': countries}


def category_context_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}
