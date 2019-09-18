from ingredient import Ingredient

class Recipe:

    def __init__(self, name, meal, ingredients):
        self.name = name
        self.meal = meal
        self.ingredients = ingredients #maybe should be pointer to ingredients, instead of duplicating

    def add_ingredient(self, name, cost, location):
        ing = Ingredient(name, cost, location)
        self.ingredients.append(ing)

    def cost(self):
        cost = 0
        for ingr in self.ingredients:
            cost = cost + float(ingr.cost)
        return cost
