import itertools

class Recipe:
    newid = itertools.count().__next__

    def __init__(self, name, meal, ingredients, tags):
        self.id = Recipe.newid()
        self.name = name
        self.meal = meal
        self.ingredients = ingredients
        self.tags = tags

    # def cost_per_serving(self):
    #     return sum(ingr.cost_per_serving() for ingr in self.ingredients)

    # def total_cost(self):
    #     return sum(ingr.cost for ingr in shelf.ingredients)