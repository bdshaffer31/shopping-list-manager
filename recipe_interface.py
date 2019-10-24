# contains the interface for working with a selected recipe

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class RecipeInterface:

    def __init__(self, rec_id):
        self.id = rec_id

    def run(self):
        commands = { 
            'display': self.display, 
            'edit name': self.edit_name, 
            'edit meal': self.edit_meal, 
            'edit tags': self.edit_tags,
            'add ingr': self.add_ingredient, 
            'remove ingr': self.remove_ingredient,
            'select ingr': self.select_ingredient,
            'delete recipe': self.delete_recipe,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.get_rec().name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete recipe', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')
    
    def get_rec(self):
        return shelf.master_list.get_rec(self.id)

    def display(self):
        print(' name: ' + self.get_rec().name)
        print(' meal: ' + self.get_rec().meal)
        print(' tags: ', end='')
        print(*self.get_rec().tags, sep=', ')
        print(' ingredients:')
        for ing in shelf.master_list.get_ingrs_from_ids(self.get_rec().ingredients):
            print('    ' + ing.name + ': ' + ing.cost + ', ' + ing.location)

    def edit_name(self):
        new_name = input('change name to: ')
        shelf.master_list.edit_recipe_attr(self.id, 'name', new_name)

    def edit_meal(self):
        new_meal = input('change meal to: ')
        shelf.master_list.edit_recipe_attr(self.get_rec().id, 'meal', new_meal)

    def add_ingredient(self): #TODO broken! needs to add ingredient to shelf and add id to recipe
        ingredients = input('enter recipe ingrediants: ')
        ingr_name_list = ingredients.split(', ')
        
        for ingr in ingr_name_list:
            #check if ingredient sharing name exists
            found = shelf.master_list.find_ing_by_name(ingr)
            if not found:
                print('new ingredient ' + ingr + ' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                servings = input('enter ingrediant servings: ')
                shelf.master_list.add_ingredient(ingr, cost, location)
                self.recipe.ingredients.append(Ingredient(ingr, cost, location, servings))
            else:
                self.recipe.ingredients.append(found)

        for rec in shelf.master_list.recipes:
            if rec.name == self.recipe.name:
                rec.ingredients = self.recipe.ingredients

    def remove_ingredient(self):
        ingr_name = input('ingredient to remove: ')
        shelf.master_list.remove_ingr_from_recipe(self.id, ingr_name)

    def edit_tags(self):
        tags = input('add tags: ').split(', ') #TODO add default value option
        shelf.master_list.edit_recipe_attr(self.id, 'tags', tags)

    def delete_recipe(self):
        shelf.master_list.delete_recipe(self.id)

    def select_ingredient(self):
        ing_name = input('select which ingredient: ')
        ingredient = [ing for ing in shelf.master_list.ingredients if ing.name == ing_name][0]
        print('-' + ingredient.name)
        ing_interface = IngredientInterface(ingredient)
        ing_interface.run()
