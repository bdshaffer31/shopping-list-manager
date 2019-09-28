# contains the interface for working with a selected ingredient

from book_shelf import shelf, BookShelf
from ingredient import Ingredient
from confirm import confirm

class IngredientInterface:

    def __init__(self, ingredient):
        self.ingredient = ingredient

    def run(self):
        commands = { 
            'display': self.display, 
            'edit name': self.edit_name,
            'edit cost': self.edit_cost,
            'edit location': self.edit_location,
            'recipes containing': self.recipes_containing,
            'delete ingr': self.delete_ingredient,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.ingredient.name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete ingr', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')

    def display(self):
        print(' name: ' + self.ingredient.name)
        print(' cost: ' + self.ingredient.cost)
        print(' location: ' + self.ingredient.lcoation)

    def edit_name(self):
        old_name = self.ingredient.name
        new_name = input('change name to: ')
        shelf.change_ingr_name(old_name, new_name)

        self.ingredient.name = new_name

    def edit_cost(self):
        new_cost = input('change cost to: ')
        shelf.change_ingr_cost(self.ingredient.name, new_cost)

        self.ingredient.cost = new_cost

    def edit_location(self):
        new_location = input('change location to: ')
        shelf.change_ingr_location(self.ingredient.name, new_location)

        self.ingredient.location = new_location

    def delete_ingredient(self):
        shelf.delete_ingredient(self.ingredient.name)

    def recipes_containing(self):
        pass