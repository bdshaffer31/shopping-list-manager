# contains the interface for working with a selected recipe

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class RecipeInterface:

    def __init__(self, recipe):
        self.recipe = recipe

    def run(self):
        commands = { 
            'display': self.display, 
            'edit name': self.edit_name, 
            'edit meal': self.edit_meal, 
            'add tags': self.add_tags,
            'add ingr': self.add_ingredient, 
            'remove ingr': self.remove_ingredient,
            'select ingr': self.select_ingredient,
            'delete recipe': self.delete_recipe,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.recipe.name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete recipe', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')
    
    def display(self):
        print(' name: ' + self.recipe.name)
        print(' meal: ' + self.recipe.meal)
        print(' tags: ', end='')
        print(*self.recipe.tags, sep=', ')
        print(' ingredients:')
        for ing in self.recipe.ingredients:
            print('    ' + ing.name + ': ' + ing.cost + ', ' + ing.location)

    def edit_name(self):
        old_name = self.recipe.name
        new_name = input('change name to: ')
        shelf.change_rec_name(old_name, new_name)

        self.recipe.name = new_name

    def edit_meal(self):
        new_meal = input('change meal to: ')
        shelf.edit_recipe_attr(self.recipe.name, 'meal', new_meal)

        self.recipe.meal = new_meal

    def add_ingredient(self): #TODO move to shelf
        ingrediants = input('enter recipe ingrediants: ')

        ingr_name_list = ingrediants.split(', ')
        
        for ingr in ingr_name_list:
            #check if ingredient sharing name exists
            found = shelf.master_list.find_ing_by_name(ingr)
            if not found:
                print('new ingredient ' + ingr + ' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                shelf.master_list.add_ingredient(ingr, cost, location)
                self.recipe.ingredients.append(Ingredient(ingr, cost, location))
            else:
                self.recipe.ingredients.append(found)

        for rec in shelf.master_list.recipes:
            if rec.name == self.recipe.name:
                rec.ingredients = self.recipe.ingredients

    def remove_ingredient(self):
        ingr_name = input('ingredient to remove: ')
        shelf.remove_ingr_from_recipe(self.recipe.name, ingr_name)

    def add_tags(self):
        tags = input('add tags: ')
        tags = tags.split(', ')
        shelf.add_rec_tags(self.recipe.name, tags)

    def delete_recipe(self):
        shelf.delete_recipe(self.recipe.name)

    def select_ingredient(self):
        ing_name = input('select which ingredient: ')
        ingredient = [ing for ing in shelf.master_list.ingredients if ing.name == ing_name ]
        ingredient = ingredient[0]
        print(ingredient.name)
        ing_interface = IngredientInterface(ingredient)
        ing_interface.run()
