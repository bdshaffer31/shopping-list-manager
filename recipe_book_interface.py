# contains the interface for working with a selected recipe book
# CARBON COPY of recipe interface

from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class RecipeBookInterface:

    def __init__(self, book):
        self.seeder = Seeder()
        self.book = book

    def run(self):
        while(True):
            action = input('input action for recipe book: ')
            if action == 'help':
                print('-help \n-exit \n-display \n-edit name \n-edit meal \n-add recipes', 
                '\n-remove recipe \n-elete recipe book')
            elif action == 'display':
                self.display()
            elif action == 'edit name':
                self.edit_name()
            elif action == 'add recipes':
                self.add_recipes()
            elif action == 'remove recipe':
                self.remove_recipe()
            elif action == 'delete recipe book':
                self.delete_recipe_book()
                break
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')
    
    def display(self):
        print(' name: ' + self.book.name)
        print(' recipes:')
        for rec in self.book.recipes:
            print('    ' + rec)
            
    def add_random_daily_menu(self): # going to add entirely new menu (needs fixed)
        shelf = self.setup_and_seed('create random daily menu')
        daily_menu = shelf.create_ran_daily_rb()
        for recipe_name in daily_menu.recipes:
            print(' - ' + recipe_name)
        shelf.recipe_books.append(daily_menu)
        self.seeder.update_seed(shelf)

    def edit_name(self): # needs cleaned up significantly map or list comprehension?
        shelf = self.setup_and_seed('edit book name')

        old_name = self.book.name
        new_name = input('change name to: ')
        shelf.change_book_name(old_name, new_name)

        self.book.name = new_name
        self.seeder.update_seed(shelf)

    def add_recipes(self):
        shelf = self.setup_and_seed('add recipes')
        recipes = input('enter recipes to add: ')

        rec_name_list = recipes.split(', ')

        #check if ingredient sharing name exists
        for rec in rec_name_list:
            found = shelf.master_list.find_rec_by_name(rec)
            if not found:
                pass
                # won't create recipes that don't exist yet :/
            else:
                self.book.recipes.append(found.name)

        for book in shelf.recipe_books:
            if book.name == self.book.name:
                book.recipes = self.book.recipes

        self.seeder.update_seed(shelf)

    def remove_recipe(self):
        pass

    def delete_recipe_book(self):
        pass

    def setup_and_seed(self, confirm_message):
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm(confirm_message)==False: 
            exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf