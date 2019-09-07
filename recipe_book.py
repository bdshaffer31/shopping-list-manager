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

    def find_ing_by_name(self, ingredient_name):
        for item in self.ingredients:
            if ingredient_name == item.name: return True
        return False #if it hasn't returned true by now

    def find_recipes_by_meal(self, meal): #used to be split into breakfast, lunch, dinner, now flexible (better?)
        recipe_list = []
        for rec in self.recipes:
            if rec.meal == meal: recipe_list.append(rec)
        return recipe_list
