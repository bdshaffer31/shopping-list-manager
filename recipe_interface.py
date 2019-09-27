# contains the interface for working with a selected recipe

from seeder import Seeder
from book_shelf import BookShelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class RecipeInterface:

    def __init__(self, recipe):
        self.seeder = Seeder()
        self.recipe = recipe

    def run(self):
        while(True):
            action = input('input action for recipe: ')
            if action == 'help':
                print('-help \n-exit \n-display \n-edit name \n-edit meal \n-add ingr', 
                '\n-remove ingr \n-select ingr \n-delete recipe')
            elif action == 'display':
                self.display()
            elif action == 'edit name':
                self.edit_name()
            elif action == 'edit meal':
                self.edit_meal()
            elif action == 'add ingr':
                self.add_ingredient()
            elif action == 'remove ingr':
                self.remove_ingredient()
            elif action == 'select ingr':
                self.select_ingredient()
            elif action == 'delete recipe':
                self.delete_recipe()
                break
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')
    
    def display(self):
        print(' name: ' + self.recipe.name)
        print(' meal: ' + self.recipe.meal)
        print(' ingredients:')
        for ing in self.recipe.ingredients:
            print('    ' + ing.name + ': ' + ing.cost + ', ' + ing.location)

    def edit_name(self): # needs cleaned up significantly map or list comprehension?
        shelf = self.setup_and_seed(msg = 'edit recipe name')

        old_name = self.recipe.name
        new_name = input('change name to: ')
        shelf.change_rec_name(old_name, new_name)

        self.recipe.name = new_name
        self.seeder.update_seed(shelf)

    def edit_meal(self):
        shelf = self.setup_and_seed(msg = 'edit recipe meal')

        new_meal = input('change meal to: ')
        shelf.change_rec_meal(self.recipe.name, new_meal)

        self.recipe.name = new_meal
        self.seeder.update_seed(shelf)

    def add_ingredient(self):
        shelf = self.setup_and_seed(msg = 'add ingredients')
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
                self.recipe.ingredients.append(Ingredient(ingr, cost, location))
            else:
                self.recipe.ingredients.append(found)

        for rec in shelf.master_list.recipes:
            if rec.name == self.recipe.name:
                rec.ingredients = self.recipe.ingredients

        self.seeder.update_seed(shelf)

    def remove_ingredient(self):
        shelf = self.setup_and_seed(msg = 'remove ingredient')
        ing_name = input('ingredient to remove: ')
        for rec in shelf.master_list.recipes:
            if rec.name == self.recipe.name:
                rec.ingredients = [ing for ing in rec.ingredients if ing.name != ing_name]
        
        self.seeder.update_seed(shelf)

    def delete_recipe(self):
        shelf = self.setup_and_seed(msg = 'delete recipe')
        shelf.delete_recipe(self.recipe.name)

        self.seeder.update_seed(shelf)

    def select_ingredient(self):
        shelf = self.setup_and_seed(msg = 'select ingredient')
        ing_name = input('select which ingredient: ')
        ingredient = [ing for ing in shelf.master_list.ingredients if ing.name == ing_name ]
        ingredient = ingredient[0]
        print(ingredient.name)
        ing_interface = IngredientInterface(ingredient)
        ing_interface.run()

    def setup_and_seed(self, **kwargs):
        confirm_message = kwargs.get('msg', None)
        if confirm_message != None:
            #use function confirm() from confirm.py to check if user wants to proceed
            if confirm(confirm_message)==False: 
                exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf