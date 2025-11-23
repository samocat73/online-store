from catalog.apps import CatalogConfig
from catalog.views import contacts_view, home_view, product_detail
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path("", home_view, name="home_view"),
    path("contacts/", contacts_view, name="contacts_view"),
    path("product_detail/<int:pk>", product_detail, name="product_detail"),
]
