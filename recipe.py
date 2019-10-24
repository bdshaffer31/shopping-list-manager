import itertools

class Recipe:
    newid = itertools.count().__next__

    def __init__(self, name, meal, ingredients, tags):
        self.id = Recipe.newid()
        self.name = name
        self.meal = meal
        self.ingredients = ingredients
        self.tags = tags
