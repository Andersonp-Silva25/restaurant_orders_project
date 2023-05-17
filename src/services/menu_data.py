import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        for line in self.csv_file_reader(source_path):
            dish = Dish(line['dish'], float(line['price']))
            ingredient = Ingredient(line['ingredient'])
            recipe_amount = line['recipe_amount']

            [self.add_ingredients(existing_dish, ingredient, recipe_amount) for existing_dish in self.dishes if existing_dish == dish]
            self.add_ingredients(dish, ingredient, recipe_amount)
            self.dishes.add(dish)              

    def csv_file_reader(self, path):
        with open(path, encoding="utf-8") as file:
            return list(
            csv.DictReader(file, delimiter=",", quotechar='"')
        )

    def add_ingredients(self, dish: Dish, ingredient, amount):
        return dish.add_ingredient_dependency(ingredient, int(amount))       