from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild in self.fields.values():
            if isinstance(fild, BooleanField):
                fild.widget.attrs.update({"class": "form-check-input"})
            else:
                fild.widget.attrs.update({"class": "form-control"})


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def clean_price(self):
        price = super().clean()["price"]
        if price < 0:
            raise ValidationError("Цена не может быть меньше 0")
        return price

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError("Нельзя вводить запрещенные слова")
        return description

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError("Нельзя вводить запрещенные слова")
        return name


class ProductFormLimited(ProductForm):
    class Meta:
        model = Product
        exclude = ("publication_status", "owner")
