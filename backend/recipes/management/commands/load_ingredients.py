import json

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = ' Загрузка ингредиентов '

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Старт загрузки ингредиентов'))
        with open('ingredients.json', encoding='utf-8') as ingredients:
            ingredient_data = json.loads(ingredients.read())
            for item in ingredient_data:
                Ingredient.objects.get_or_create(**item)
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
