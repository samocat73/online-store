from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(upload_to="catalog/photo/", verbose_name="Фотография")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    publication_status = models.BooleanField(
        default=False, verbose_name="Флаг для публикации"
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [("can_unpublish_product", "Can unpublish product")]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
