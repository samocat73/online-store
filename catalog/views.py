from catalog.models import Product
from django.views.generic import TemplateView, ListView, DetailView


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
