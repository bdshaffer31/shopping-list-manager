# contains the interface for working with a selected recipe book

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class BookInterface:

    def __init__(self, book):
        self.book = book

    def run(self):
        commands = { 
            'display': self.display, 
            'edit name': self.edit_name,
            'add recipes': self.add_recipes,
            'remove recipe': self.remove_recipe,
            'shopping list': self.gen_shopping_list,
            'delete book': self.delete_book,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.book.name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete book', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
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

    def edit_name(self): 
        new_name = input('change name to: ')
        shelf.edit_book_attr(self.book.name, 'name', new_name)

        self.book.name = new_name

    def add_recipes(self): #needs to be moved up?
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
        shelf.remove_recipe_from_book(self.book.name, recipe_name)

    def delete_book(self):
        shelf.delete_book(self.book.name)

    def gen_shopping_list(self):
        shopping_list = shelf.shopping_list(shelf.book_ingr_list(self.book))

        #ADD write to text file
        for ingr in shopping_list:
            print(' - ' + ingr.name)