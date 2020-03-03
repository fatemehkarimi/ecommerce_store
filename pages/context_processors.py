from products.models import Category, SubCategory

def nav_bar_context(request):
    categories = Category.objects.exclude(category_name='Unknown')
    subcategories = SubCategory.objects.all()
    return {
        'categories': categories,
        'subcategories': subcategories
    }