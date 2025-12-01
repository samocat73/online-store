from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError

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


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["photo"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-select"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})

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
