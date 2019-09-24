from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from recipe_interface import RecipeInterface
from ingredient_interface import IngredientInterface
from recipe_book_interface import RecipeBookInterface
from confirm import confirm

class ShelfInterface:

    def __init__(self):
        self.seeder = Seeder()

    def run(self):
        while(True):
            action = input('input action: ')
            if action == 'help':
                print('-help \n-exit \n-display recipes \n-display \n-create recipe \n-display meal',
                '\n-add daily menu \n-display recipe costs \n-edit ingr \n-add menu',
                '\n-remove menu \n-select menu')
            elif action == 'display recipes':
                self.display_recipes()
            elif action == 'display':
                self.display()
            elif action == 'create recipe':
                self.create_recipe()
            elif action == 'display meal':
                self.display_meal()
            elif action == 'display recipe costs':
                self.display_recipe_costs()
            elif action == 'select recipe':
                self.input_select_recipe()
            elif action == 'select ingr':
                self.input_select_ingredient()
            elif action == 'add menu':
                self.add_recipe_book()
            elif action == 'remove menu': #maybe this should be called delete for continuity
                self.remove_recipe_book()
            elif action == 'select menu':
                self.input_select_recipe_book()
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
    
    def display_meal(self):
        shelf = self.setup_and_seed('view recipe book contents')
        meal = input('display all recipes for which meal:')
        rec_list = shelf.master_list.find_recipes_by_meal(meal)
        self.print_recipes(rec_list)

    def display_recipes(self):
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_recipes(shelf.master_list.recipes)

    def display(self):
        shelf = self.setup_and_seed('view recipe book contents')
        for book in shelf.recipe_books:
            print(book.name)

    def display_recipe_costs(self):
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_costs(shelf.master_list.recipes)

    def add_recipe_book(self):
        shelf = self.setup_and_seed('create new recipe book')
        name = input('recipe book name:')
        shelf.add_recipe_book(name, [])
        self.seeder.update_seed(shelf)
        self.select_recipe_book(name)

    def remove_recipe_book(self):
        pass

    def input_select_recipe_book(self):
        name = input('select which recipe book:')
        self.select_recipe_book(name)

    def select_recipe_book(self, name):
        shelf = self.setup_and_seed('select recipe book')
        book = [book for book in shelf.recipe_books if book.name == name]
        book = book[0]
        recb_interface = RecipeBookInterface(book)
        recb_interface.run()

    def input_select_recipe(self):
        recipe_name = input('select which recipe:')
        self.select_recipe(recipe_name)

    def select_recipe(self, recipe_name):
        shelf = self.setup_and_seed('select recipe')
        recipe = [rec for rec in shelf.master_list.recipes if rec.name == recipe_name]
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