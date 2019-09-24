from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from recipe_interface import RecipeInterface
from ingredient_interface import IngredientInterface
from confirm import confirm

class Interface:

    def __init__(self):
        self.seeder = Seeder()

    def run(self):
        while(True):
            action = input('input action: ')
            if action == 'help':
                print('-help \n-exit \n-display recipes \n-create recipe \n-display meal',
                '\n-add daily menu \n-display recipe costs \n-edit ingr')
            elif action == 'display recipes':
                self.display_recipes()
            elif action == 'create recipe':
                self.create_recipe()
            elif action == 'display meal':
                self.display_meal()
            elif action == 'add daily menu':
                self.add_random_daily_menu()
            elif action == 'display recipe costs':
                self.display_recipe_costs()
            elif action == 'select recipe':
                self.select_recipe()
            elif action == 'select ingr':
                self.select_ingredient()
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')

    def create_recipe(self): 
        shelf = self.setup_and_seed('create new recipe')

        name = input('enter recipe name: ')
        meal = input('enter recipe meal: ').lower()
        ingredients = input('enter recipe ingredients: ')

        ingr_name_list = ingredients.split(', ')
        ingr_list = []

        #check if ingredient sharing name exists
        for ingr in ingr_name_list:
            found = shelf.master_list.find_ing_by_name(ingr)
            if not found:
                print('new ingredient ' + ingr + ' enter additional info')
                cost = input('enter ingredient cost: ')
                location = input('enter ingredient location: ')
                shelf.master_list.add_ingredient(ingr, cost, location)
                ingr_list.append(Ingredient(ingr, cost, location))
            else:
                ingr_list.append(found)

        shelf.master_list.add_recipe(name, meal, ingr_list)
        self.seeder.update_seed(shelf)
    
    def display_meal(self):
        shelf = self.setup_and_seed('view recipe book contents')
        meal = input('display all recipes for which meal:')
        rec_list = shelf.master_list.find_recipes_by_meal(meal)
        self.print_recipes(rec_list)

    def display_recipes(self):
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_recipes(shelf.master_list.recipes)

    def display_recipe_costs(self):
        shelf = self.setup_and_seed('view recipe book contents')
        self.print_costs(shelf.master_list.recipes)

    def add_random_daily_menu(self):
        shelf = self.setup_and_seed('create random daily menu')
        daily_menu = shelf.create_ran_daily_rb()
        for recipe_name in daily_menu.recipes:
            print(' - ' + recipe_name)
        shelf.recipe_books.append(daily_menu)
        self.seeder.update_seed(shelf)

    def select_recipe(self):
        shelf = self.setup_and_seed('select recipe')
        recipe_name = input('select which recipe:')
        recipe = [rec for rec in shelf.master_list.recipes if rec.name == recipe_name]
        recipe = recipe[0]
        print(recipe.name)
        rec_interface = RecipeInterface(recipe)
        rec_interface.run()

    def select_ingredient(self):
        shelf = self.setup_and_seed('select ingredient')
        ing_name = input('select which ingredient:')
        ing = [ing for ing in shelf.master_list.ingredients if ing.name == ing_name]
        ing = ing[0]
        print(ing.name)
        ing_interface = IngredientInterface(ing)
        ing_interface.run()

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