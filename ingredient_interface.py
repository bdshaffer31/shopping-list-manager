# contains the interface for working with a selected recipe
#CURRENTLY JUST CARBON COPY OF RECIPE INTERFACE

from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from confirm import confirm

class IngredientInterface:

    def __init__(self, ingredient):
        self.seeder = Seeder()
        self.ingredient = ingredient

    def run(self):
        while(True):
            action = input('input action: ')
            if action == 'help':
                print('help \nexit \nedit_name \nedit_meal \nadd_ingredients', 
                '\nremove_ingredient \nselect_ingredient \n delete_recipe')
            elif action == 'edit_name':
                self.edit_name()
            elif action == 'edit_meal':
                self.edit_meal()
            elif action == 'add_ingredients':
                self.add_ingredients()
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
        pass

    def edit_meal(self):
        pass

    def add_ingredients(self):
        pass

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