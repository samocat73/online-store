from catalog.apps import CatalogConfig
from catalog.views import home_view, contacts_view
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path("", home_view, name="home_view"),
    path("contacts/", contacts_view, name="contacts_view"),
]
