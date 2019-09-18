from recipe import Recipe
from ingredient import Ingredient

class RecipeBook:

    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes
        self.ingredients = [] # TODO make this from recipes in init

    def add_recipe(self, name): #TODO add check if recipe already exists, this is not really needed anymore
        self.recipes.append(name)

    def add_ingredient(self, name): #TODO add check if ingredient already exists, this is not really needed anymore
        self.ingredients.append(name)

    def find_ing_by_name(self, ingredient_name): # this was changed and that broke some things 
        for ing in self.ingredients:
            if ingredient_name == ing: return ing
        return False #if it hasn't returned the ingredient by now

    def find_recipes_by_meal(self, meal): #used to be split into breakfast, lunch, dinner, now flexible (better?)
        recipe_list = []
        for rec in self.recipes:
            if rec.meal == meal: recipe_list.append(rec)
        return recipe_list
