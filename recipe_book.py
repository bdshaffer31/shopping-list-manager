from recipe import Recipe
from ingredient import Ingredient
class RecipeBook:

    def __init__(self):
        self.recipes = []
        self.ingredients = []

    def populate_from_seed(self):
        #read the seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")
        #parse the seed file turning everything into ingredents then recipes
        adding_recipes = False
        for aline in seed_file:
            if not adding_recipes:
                if len(aline) > 1 and not aline.isspace() and aline[0] != '=':
                    comps = aline.split(" | ")
                    self.add_ingredient(comps[0], comps[1], comps[2])
                elif aline[0] == '=':
                    adding_recipes = True
            else:
                if len(aline) > 1 and not aline.isspace():
                    comps = aline.split(" | ")
                    raw_list = comps[2].split(',')
                    ingredient_list = [item.strip() for item in raw_list if item.strip()]
                    self.add_recipe(comps[0], comps[1], ingredient_list)

    def update_seed(self):
        #get ready to write in seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')
        #write the ingredients first
        for item in self.ingredients:
            seed_file.writelines(item.name + ' | ' + item.cost + ' | ' + item.location + ' | \n')
        #then write the recipes
        seed_file.writelines("===== Recipes =====\n")
        for item in self.recipes:
            seed_file.writelines(item.name + ' | ' + item.meal + ' | ') 
            for ingr in item.ingredients: 
                seed_file.writelines(ingr + ', ')
            seed_file.writelines(' | \n')
        seed_file.close

    def add_recipe(self, name, meal, ingredients):
        self.recipes.append(Recipe(name, meal, ingredients))

    def add_ingredient(self, name, cost, location):
        self.ingredients.append(Ingredient(name, cost, location))

