from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from recipe_interface import RecipeInterface
from ingredient_interface import IngredientInterface
from book_interface import BookInterface
from confirm import confirm

class ShelfInterface:

    def __init__(self):
        pass

    def run(self):
        commands = { 
            'display recipes': self.display_recipes, 
            'display': self.display, 
            'display by criteria': self.display_by_criteria,
            'create recipe': self.create_recipe, 
            'select recipe': self.input_select_recipe, 
            'select ingr': self.input_select_ingredient, 
            'create ingr': self.create_ingredient,
            'create book': self.create_book,
            'select book': self.input_select_book,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action: ')
            if action in commands:
                commands[action]()
                if action in ['exit']:
                    #shelf.write_for_humans()
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')

    def display(self):
        for book in shelf.books:
            print(' - ' + book.name)

    def create_recipe(self): 

        name = input('enter recipe name: ')
        meal = input('enter recipe meal: ').lower()
        tags = input('enter recipe tags: ').split(', ')

        shelf.master_list.add_recipe(name, meal, [], tags)
        self.select_recipe(name)

    def create_ingredient(self):
        pass

    def display_recipes(self):
        self.print_recipes(shelf.master_list.recipes)

    def create_book(self):
        name = input('recipe book name: ')
        shelf.add_book(name, [])
        self.select_book(name)

    def input_select_book(self):
        name = input('select which recipe book: ')
        self.select_book(name)

    def select_book(self, name):
        try:
            book = [book for book in shelf.books if book.name == name][0]
        except IndexError:
            print('book with name \'' + name + '\' not found')
            return
        
        recb_interface = BookInterface(book.id)
        recb_interface.run()

    def input_select_recipe(self):
        recipe_name = input('select which recipe: ')
        self.select_recipe(recipe_name)

    def select_recipe(self, name):
        try:
            recipe = [rec for rec in shelf.master_list.recipes if rec.name == name][0]
        except IndexError:
            print('recipe with name \'' + name + '\' not found')
            return

        rec_interface = RecipeInterface(recipe.id)
        rec_interface.run()
        
    def input_select_ingredient(self):
        ingr_name = input('select which ingredient: ')
        self.select_ingredient(ingr_name)

    def select_ingredient(self, name):
        try:
            ingr = [ingr for ingr in shelf.master_list.ingredients if ingr.name == name][0]
        except IndexError:
            print('ingredient with name \'' + name + '\' not found')
            return
        
        ingr_interface = IngredientInterface(ingr.id)
        ingr_interface.run()

    def print_costs(self, rec_list):
        for rec in rec_list:
            print("- " + rec.name + " - $" + str(rec.cost()))

    def print_recipes(self, rec_list):
        for rec in rec_list:
            print("- " + rec.name + " - ", end = "")
            for ing in shelf.master_list.get(shelf.master_list.ingredients, rec.ingredients):
                print(ing.name + ", ", end = "")
            print()

    def display_by_criteria(self): # is returning union not intersection
        meal = input('get recipes for which meal (any if blank): ')
        tags = input('get recipes for which tags (any if blank): ').split(', ')
        recs = shelf.master_list.get_by_criteria(meal, tags)
        self.print_recipes(recs)

    def display_meal(self): #no longer and option from input
        meal = input('display all recipes for which meal: ')
        rec_list = shelf.master_list.find_recipes_by_meal(meal)
        self.print_recipes(rec_list)

    def display_recipe_costs(self): # no longer and option from input
        self.print_costs(shelf.master_list.recipes)