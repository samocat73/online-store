from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm, ProductFormLimited
from catalog.models import Product


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home_view")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy("catalog:home_view")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("can_unpublish_product"):
            return ProductForm
        else:
            return ProductFormLimited

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.owner == self.request.user or self.request.user.has_perm(
            "can_unpublish_product"
        ):
            return obj
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home_view")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.owner == self.request.user or self.request.user.has_perm(
            "catalog.delete_product"
        ):
            return obj
        else:
            raise PermissionDenied
