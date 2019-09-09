from ingredient import Ingredient

class Recipe:

    def __init__(self, name, meal, ingredients):
        self.name = name
        self.meal = meal
        self.ingredients = ingredients #actually just a string list of ingredient names

    def add_ingredient(self, name, cost, location):
        ing = Ingredient(name, cost, location)
        self.ingredients.append(ing)
