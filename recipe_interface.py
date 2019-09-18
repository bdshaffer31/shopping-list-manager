# contains the interface for working with a selected recipe

from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from confirm import confirm

class RecipeInterface:

    def __init__(self, recipe):
        self.seeder = Seeder()
        self.recipe = recipe

    def run(self):
        while(True):
            action = input('input action for recipe: ')
            if action == 'help':
                print('-help \n-exit \n-edit_name \n-edit_meal \n-add_ingredient', 
                '\n-remove_ingredient \n-select_ingredient \n-delete_recipe')
            elif action == 'edit_name':
                self.edit_name()
            elif action == 'edit_meal':
                self.edit_meal()
            elif action == 'add_ingredient':
                self.add_ingredient()
            elif action == 'remove_ingredient':
                self.remove_ingredient()
            elif action == 'select_ingredient':
                self.select_ingredient()
            elif action == 'delete recipe':
                self.delete_recipe()
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')

    def edit_name(self):
        shelf = self.setup_and_seed('edit recipe name')

        name = input('change name to:')
        self.recipe.name = name
        shelf.seeder.update_seed(shelf)

    def edit_meal(self):
        pass

    def add_ingredient(self):
        shelf = self.setup_and_seed('add ingredients')
        ingrediants = input('enter recipe ingrediants: ')

        ingr_name_list = ingrediants.split(', ')

        #check if ingredient sharing name exists
        for ingr in ingr_name_list:
            found = shelf.master_list.find_ing_by_name(ingr)
            if not found:
                print('new ingredient ' + ingr + ' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                shelf.master_list.add_ingredient(ingr, cost, location)
                self.recipe.ingrediants.append(Ingredient(ingr, cost, location))
            else:
                self.recipe.ingredients.append(found)

        self.seeder.update_seed(shelf)

    def remove_ingredient(self):
        pass

    def select_ingredient(self):
        pass

    def delete_recipe(self):
        pass

    def setup_and_seed(self, confirm_message):
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm(confirm_message)==False: 
            exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf