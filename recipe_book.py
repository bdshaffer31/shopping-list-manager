from recipe import Recipe
from ingredient import Ingredient

class RecipeBook:

    def __init__(self, name, recipes, ingredients):
        self.name = name
        self.recipes = recipes
        self.ingredients = ingredients

    def add_recipe(self, name, meal, ingredients): #TODO add check if recipe already exists
        self.recipes.append(Recipe(name, meal, ingredients))

    def add_ingredient(self, name, cost, location): #TODO add check if ingredient already exists
        self.ingredients.append(Ingredient(name, cost, location))

