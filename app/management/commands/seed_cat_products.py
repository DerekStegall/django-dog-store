from django.core.management.base import BaseCommand, CommandError
from app import models

CAT_PRODUCTS = [
    {
        "name": "SPICY catnip",
        "product_type": "treat",
        "cat_size": "big cats",
        "price": 1.55,
        "quantity": 18,
    },
    {
        "name": "Catato Chips",
        "product_type": "treat",
        "cat_size": "all cats",
        "price": 0.88,
        "quantity": 33,
    },
    {
        "name": "squeaker mouse",
        "product_type": "toy",
        "cat_size": "small cats",
        "price": 5.44,
        "quantity": 10,
    },
    {
        "name": "scratch post",
        "product_type": "toy",
        "cat_size": "big cats",
        "price": 6.33,
        "quantity": 10,
    },
    {
        "name": "scatch ball",
        "product_type": "toy",
        "cat_size": "all cats",
        "price": 8.88,
        "quantity": 5,
    },
    {
        "name": "sizzled tuna",
        "product_type": "treat",
        "cat_size": "small cats",
        "price": 3.50,
        "quantity": 22,
    },
    {
        "name": "big fish",
        "product_type": "treat",
        "cat_size": "big cats",
        "price": 4.00,
        "quantity": 16,
    },
    {
        "name": "fishing line",
        "product_type": "toy",
        "cat_size": "all cats",
        "price": 0.99,
        "quantity": 43,
    },
    {
        "name": "ball tower",
        "product_type": "toy",
        "cat_size": "all cats",
        "price": 1.49,
        "quantity": 37,
    },
]

class Command(BaseCommand):
    help = (
        "Seeds the database with cat products based on the cat store python benchmark"
    )

    def handle(self, *args, **options):
        for cat_product in CAT_PRODUCTS:
            self.create_cat_product(cat_product)

    def create_cat_product(self, cat_product_data: dict):
        name = cat_product_data.pop("name")
        movie, created = models.CatProduct.objects.get_or_create(
            name=name, defaults=cat_product_data
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"{name} created"))
        else:
            self.stdout.write(f"{name} already exists")