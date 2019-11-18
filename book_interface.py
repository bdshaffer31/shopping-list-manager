# contains the interface for working with a selected recipe book

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from recipe import Recipe
from confirm import confirm
from ingredient_interface import IngredientInterface

class BookInterface:

    def __init__(self, book_id):
        self.id = book_id

    def run(self):
        commands = { 
            'display': self.display, 
            'edit name': self.edit_name,
            'add recipes': self.add_recipes,
            'remove recipe': self.remove_recipe,
            'shopping list': self.gen_shopping_list,
            'add days': self.add_days,
            'add by criteria': self.add_by_criteria,
            'delete book': self.delete_book,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.get_book().name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete book', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')

    def get_book(self):
        return shelf.get_book(self.id)
    
    def display(self):
        print(' name: ' + self.get_book().name)
        print(' recipes:')
        for rec in shelf.master_list.get(shelf.master_list.recipes, self.get_book().recipes):
            print('    ' + rec.name)
            
    def add_random_daily_menu(self): # going to add entirely new menu (needs fixed)
        daily_menu = shelf.create_ran_daily_rb()
        for recipe_name in daily_menu.recipes:
            print(' - ' + recipe_name)
        shelf.books.append(daily_menu)

    def edit_name(self): 
        new_name = input('change name to: ')
        shelf.edit_book_attr(self.id, 'name', new_name)

    def add_recipes(self): #needs to be moved up?
        recipes = input('enter recipes to add: ')

        rec_name_list = recipes.split(', ')

        #check if ingredient sharing name exists
        for rec in rec_name_list:
            found = shelf.master_list.find_rec_by_name(rec)
            if not found:
                meal = input('enter recipe meal: ').lower()
                tags = input('enter recipe tags: ').split(', ')

                new_rec = Recipe(rec, meal, [], tags)
                shelf.master_list.recipes.append(new_rec)
                self.get_book().recipes.append(new_rec.id)
            else:
                self.get_book().recipes.append(found.id)


    def remove_recipe(self):
        recipe_name = input('enter recipe to remove: ').strip()
        shelf.remove_recipe_from_book(self.id, shelf.master_list.find_rec_by_name(recipe_name).id)

    def delete_book(self):
        shelf.delete_book(self.id)

    def gen_shopping_list(self):
        shopping_list = shelf.sorted_shopping_list(shelf.book_ingr_list(self.id))

        #ADD write to text file
        for ingr in shopping_list:
            print(' - ' + ingr.name)

    def add_by_criteria(self):
        meal = input('get recipes for which meal (any if blank): ')
        tags = input('get recipes for which tags (any if blank): ')
        tags = list(filter(None, tags.split('/')))
        number = int(input('how many recipes to add: '))
        shelf.add_by_criteria(self.id, number, meal, tags)
        
    def add_days(self):
        days = int(input('how many random days to add: '))
        shelf.add_ran_daily_plans(self.id, days)