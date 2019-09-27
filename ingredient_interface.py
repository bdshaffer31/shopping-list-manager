# contains the interface for working with a selected ingredient

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
            action = input('input action for ingr: ')
            if action == 'help':
                print('help \nexit \nedit name \nedit cost \nedit location', 
                '\ndelete ingr \nrecipes containing \ndelete recipe')
            elif action == 'edit name':
                self.edit_name()
            elif action == 'edit cost':
                self.edit_cost()
            elif action == 'edit location':
                self.edit_location()
            elif action == 'delete ingr':
                self.delete_ingredient()
            elif action == 'recipes containing':
                self.recipes_containing()
            elif action == 'delete ingredient':
                pass
                #self.delete_recipe()
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')

    def edit_name(self):
        shelf = self.setup_and_seed(msg = 'edit ingredient name')

        old_name = self.ingredient.name
        new_name = input('change name to: ')
        shelf.change_ingr_name(old_name, new_name)

        self.ingredient.name = new_name
        self.seeder.update_seed(shelf)

    def edit_cost(self):
        shelf = self.setup_and_seed(msg = 'edit ingredient cost')

        new_cost = input('change cost to: ')
        shelf.change_ingr_cost(self.ingredient.name, new_cost)

        self.ingredient.cost = new_cost
        self.seeder.update_seed(shelf)

    def edit_location(self):
        shelf = self.setup_and_seed(msg = 'edit ingredient location')

        new_location = input('change location to: ')
        shelf.change_ingr_location(self.ingredient.name, new_location)

        self.ingredient.location = new_location
        self.seeder.update_seed(shelf)

    def delete_ingredient(self):
        pass

    def recipes_containing(self):
        pass

    def setup_and_seed(self, **kwargs):
        confirm_message = kwargs.get('msg', None)
        if confirm_message != None:
            #use function confirm() from confirm.py to check if user wants to proceed
            if confirm(confirm_message)==False: 
                exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf