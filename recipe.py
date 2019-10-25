import itertools
from uuid import uuid4

class Recipe:
    newid = itertools.count().__next__

    def __init__(self, name, meal, ingredients, tags):
        #self.id = Recipe.newid()
        self.id = uuid4().hex
        self.name = name
        self.meal = meal
        self.ingredients = ingredients
        self.tags = tags
