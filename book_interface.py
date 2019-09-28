# contains the interface for working with a selected recipe book

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class BookInterface:

    def __init__(self, book):
        self.book = book

    def run(self):
        while(True):
            action = input('input action for recipe book: ')
            if action == 'help':
                print('-help \n-exit \n-display \n-edit name \n-add recipes', 
                '\n-remove recipe \n-delete book \n-shopping list')
            elif action == 'display':
                self.display()
            elif action == 'edit name':
                self.edit_name()
            elif action == 'add recipes':
                self.add_recipes()
            elif action == 'remove recipe':
                self.remove_recipe()
            elif action == 'delete book':
                self.delete_book()
                break
            elif action == 'shopping list':
                self.gen_shopping_list()
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
        daily_menu = shelf.create_ran_daily_rb()
        for recipe_name in daily_menu.recipes:
            print(' - ' + recipe_name)
        shelf.books.append(daily_menu)

    def edit_name(self): # needs cleaned up significantly map or list comprehension?
        old_name = self.book.name
        new_name = input('change name to: ')
        shelf.change_book_name(old_name, new_name)

        self.book.name = new_name

    def add_recipes(self):
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

        for book in shelf.books:
            if book.name == self.book.name:
                book.recipes = self.book.recipes

    def remove_recipe(self):
        recipe_name = input('enter recipe to remove: ').strip()

        for book in shelf.books:
            if book.name == self.book.name:
                book.recipes = [rec for rec in book.recipes if rec != recipe_name]

    def delete_book(self):
        pass

    def gen_shopping_list(self):
        ingr_list = shelf.book_ingr_list(self.book)
        shopping_list = shelf.shopping_list(ingr_list)

        #ADD write to text file
        for ingr in shopping_list:
            print(ingr.name)

    # def setup_and_seed(self, **kwargs):
    #     confirm_message = kwargs.get('msg', None)
    #     if confirm_message != None:
    #         #use function confirm() from confirm.py to check if user wants to proceed
    #         if confirm(confirm_message)==False: 
    #             exit()
    #     self.seeder.refresh_seed()
    #     shelf = self.seeder.populate_bookshelf()
    #     return shelf