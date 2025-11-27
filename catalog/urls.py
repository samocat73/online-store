from catalog.apps import CatalogConfig
from catalog.views import ContactView, ProductListView, ProductDetailView
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home_view"),
    path("contacts/", ContactView.as_view(), name="contacts_view"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
