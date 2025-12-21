from catalog.models import Product


def products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)
