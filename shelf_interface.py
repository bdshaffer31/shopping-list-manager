from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from recipe_interface import RecipeInterface
from ingredient_interface import IngredientInterface
from book_interface import BookInterface
from confirm import confirm

class ShelfInterface:

    def __init__(self):
        self.seeder = Seeder()

    def run(self):
        while(True):
            action = input('input action: ')
            if action == 'help':
                print('-help \n-exit \n-display recipes \n-display \n-create recipe ',
                '\n-select ingr \n-select recipe \n-create recipe \n-add book',
                '\n-remove book \n-select book')
            elif action == 'display recipes':
                self.display_recipes()
            elif action == 'display':
                self.display()
            elif action == 'create recipe':
                self.create_recipe()
            elif action == 'select recipe':
                self.input_select_recipe()
            elif action == 'select ingr':
                self.input_select_ingredient()
            elif action == 'add book':
                self.add_book()
            elif action == 'remove book': #maybe this should be called delete for continuity
                self.remove_book()
            elif action == 'select book':
                self.input_select_book()
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')

    def create_recipe(self): 
        shelf = self.setup_and_seed('create new recipe')

        name = input('enter recipe name: ')
        meal = input('enter recipe meal: ').lower()

        shelf.master_list.add_recipe(name, meal, [])
        self.seeder.update_seed(shelf)
        self.select_recipe(name)

    def display_recipes(self):
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_recipes(shelf.master_list.recipes)

    def display(self):
        shelf = self.setup_and_seed('view recipe book contents')
        for book in shelf.books:
            print(book.name)

    def add_book(self):
        shelf = self.setup_and_seed('create new recipe book')
        name = input('recipe book name:')
        shelf.add_book(name, [])
        self.seeder.update_seed(shelf)
        self.select_book(name)

    def remove_book(self):
        pass

    def input_select_book(self):
        name = input('select which recipe book:')
        self.select_book(name)

    def select_book(self, name):
        shelf = self.setup_and_seed('select recipe book')
        book = [book for book in shelf.books if book.name == name]
        book = book[0]
        recb_interface = BookInterface(book)
        recb_interface.run()

    def input_select_recipe(self):
        recipe_name = input('select which recipe:')
        self.select_recipe(recipe_name)

    def select_recipe(self, recipe_name):
        shelf = self.setup_and_seed('select recipe')
        try:
            recipe = [rec for rec in shelf.master_list.recipes if rec.name == recipe_name]
        except:
            print('recipe with name \'' + recipe_name + '\' not found')
            return

        recipe = recipe[0]
        rec_interface = RecipeInterface(recipe)
        rec_interface.run()
        
    def input_select_ingredient(self):
        ingr_name = input('select which ingredient:')
        self.select_recipe(ingr_name)

    def select_ingredient(self, ingr_name):
        shelf = self.setup_and_seed('select ingredient')
        ingr = [ingr for ingr in shelf.master_list.ingredients if ingr.name == ingr_name]
        ingr = ingr[0]
        ingr_interface = IngredientInterface(ingr)
        ingr_interface.run()

    def print_costs(self, rec_list):
        for rec in rec_list:
            print("- " + rec.name + " - $" + str(rec.cost()))

    def print_recipes(self, rec_list):
        for rec in rec_list:
            print("- " + rec.name + " - ", end = "")
            for ing in rec.ingredients:
                print(ing.name + ", ", end = "")
            print()

    def setup_and_seed(self, confirm_message):
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm(confirm_message)==False: 
            exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf

    def display_meal(self): #no longer and option from input
        shelf = self.setup_and_seed('view recipe book contents')
        meal = input('display all recipes for which meal:')
        rec_list = shelf.master_list.find_recipes_by_meal(meal)
        self.print_recipes(rec_list)

    def display_recipe_costs(self): # no longer and option from input
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_costs(shelf.master_list.recipes)