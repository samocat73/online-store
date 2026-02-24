from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test categories and products to the database"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        washing_machines, _ = Category.objects.get_or_create(
            name="Стиральные машины", description="Стиральные машины по выгодным ценам."
        )
        irons, _ = Category.objects.get_or_create(
            name="Утюги", description="Утюги для ровного белья"
        )

        products = [
            {
                "name": "LG F2Y1NS6W",
                "description": "LG F2Y1NS6W - фронтальная стиральная машина с функцией пара.",
                "category": washing_machines,
                "price": 27999,
            },
            {
                "name": "LG FH0B8LD6",
                "description": "Стиральная машина LG FH0B8LD6 рассчитана на одновременную загрузку 5 кг белья.",
                "category": washing_machines,
                "price": 33999,
            },
            {
                "name": "Polaris PIR 2420AK",
                "description": "Утюг Polaris PIR 2420AK в стильном исполнении способен сделать процесс глажки достаточно удобным и быстрым.",
                "category": irons,
                "price": 3199,
            },
            {
                "name": "Braun TexStyle 9 SI9661VI",
                "description": "Утюг Braun TexStyle 9 SI9661VI с мощностью 3100 Вт, непрерывной подачей пара 0-60 г/мин и паровым ударом до 250 г/мин устраняет стойкие складки.",
                "category": irons,
                "price": 9699,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Product added successfully: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f"Product already exists: {product.name}")
                )
