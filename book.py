from recipe import Recipe
from ingredient import Ingredient

class Book:

    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes

    def add_recipe(self, name): #TODO add check if recipe already exists, this is not really needed anymore
        self.recipes.append(name)