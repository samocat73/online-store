from django.shortcuts import render
from catalog.models import Product


def contacts_view(request):
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context=context)


def home_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home_view.html", context=context)
