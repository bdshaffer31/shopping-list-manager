# contains the interface for working with a selected ingredient

from book_shelf import shelf, BookShelf
from ingredient import Ingredient
from confirm import confirm

class IngredientInterface:

    def __init__(self, ingredient_id):
        self.id = ingredient_id

    def run(self):
        self.display()
        commands = {
            'display': self.display,
            'edit name': self.edit_name,
            'edit cost': self.edit_cost,
            'edit location': self.edit_location,
            'edit servings': self.edit_servings,
            'recipes containing': self.recipes_containing,
            'delete ingr': self.delete_ingredient,
            'exit': shelf.update_db
            }
        while True:
            action = input('input action for ' + self.get_ingr().name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete ingr', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')
                
    def get_ingr(self):
        return shelf.master_list.get(shelf.master_list.ingredients, [self.id])[0]

    def display(self):
        print(' name: ' + self.get_ingr().name)
        print(' cost: ' + self.get_ingr().cost)
        print(' location: ' + self.get_ingr().location)
        print(' servings: ' + str(self.get_ingr().servings))

    def edit_name(self):
        new_name = input('change name to: ')
        shelf.master_list.edit_ingr_attr(self.id, 'name', new_name)

    def edit_cost(self):
        new_cost = input('change cost to: ')
        shelf.master_list.edit_ingr_attr(self.id, 'cost', new_cost)

    def edit_location(self):
        new_location = input('change location to: ')
        shelf.master_list.edit_ingr_attr(self.id, 'location', new_location)

    def edit_servings(self):
        new_servings = input('change servings to: ')
        shelf.master_list.edit_ingr_attr(self.id, 'servings', new_servings)

    def delete_ingredient(self):
        shelf.master_list.delete_ingredient(self.id)

    def recipes_containing(self):
        recs = shelf.master_list.recipes_containing(shelf.master_list.recipes, self.id)
        for rec in recs:
            print(' - ' + rec.name)