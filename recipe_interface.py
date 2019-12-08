# contains the interface for working with a selected recipe

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from confirm import confirm
from ingredient_interface import IngredientInterface

class RecipeInterface:

    def __init__(self, rec_id):
        self.id = rec_id

    def run(self):
        self.display()
        commands = {
            'display': self.display,
            'edit name': self.edit_name, 
            'edit meal': self.edit_meal, 
            'edit tags': self.edit_tags,
            'add ingr': self.add_ingredient, 
            'remove ingr': self.remove_ingredient,
            'select ingr': self.select_ingredient,
            'delete recipe': self.delete_recipe,
            'exit': shelf.update_db
            }
        while(True):
            action = input('input action for ' + self.get_rec().name + ': ')
            if action in commands:
                commands[action]()
                if action in ['delete recipe', 'exit']:
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print('input not recognized, type \'help\' for a list')
    
    def get_rec(self):
        return shelf.master_list.get(shelf.master_list.recipes, [self.id])[0]

    def display(self):
        print(' name: ' + self.get_rec().name)
        print(' meal: ' + self.get_rec().meal)
        print(' cost per serving: ' + str(shelf.master_list.cost_per_serving(self.id)))
        print(' tags: ', end='')
        print(*self.get_rec().tags, sep=', ')
        print(' ingredients:')
        for ing in shelf.master_list.get(shelf.master_list.ingredients, self.get_rec().ingredients):
            print('    ' + ing.name + ': ' + ing.cost + ', ' + ing.location)
        for rec in shelf.master_list.get(shelf.master_list.recipes, self.get_rec().ingredients):
            print('    ' + rec.name + ': ' + str(shelf.master_list.rec_total_cost(rec.id)))

    def edit_name(self):
        new_name = input('change name to: ')
        shelf.master_list.edit_recipe_attr(self.id, 'name', new_name)

    def edit_meal(self):
        new_meal = input('change meal to: ')
        shelf.master_list.edit_recipe_attr(self.get_rec().id, 'meal', new_meal)

    def add_ingredient(self): #TODO broken! needs to add ingredient to shelf and add id to recipe
        ingredients = input('enter recipe ingrediants: ')
        comp_name_list = ingredients.split(', ')
        
        for comp_name in comp_name_list:
            #check if ingredient sharing name exists
            found = shelf.master_list.find_comp_by_name(comp_name)
            if not found and comp_name is not '':
                print('new ingredient ' + comp_name + ' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                servings = input('enter ingrediant servings: ')
                new_ingr = Ingredient(comp_name, cost, location, servings)
                shelf.master_list.ingredients.append(new_ingr)
                self.get_rec().ingredients.append(new_ingr.id)
            else:
                self.get_rec().ingredients.append(found.id)

    def remove_ingredient(self):
        comp_name = input('ingredient to remove: ')
        found = shelf.master_list.find_comp_by_name(comp_name)
        if found:
            shelf.master_list.remove_ingr_from_recipe(self.id, found.id)
        else:
            print('ingredient with name \'' + comp_name + '\' not found')

    def edit_tags(self):
        tags = input('add tags: ').split(', ') #TODO add default value option
        shelf.master_list.edit_recipe_attr(self.id, 'tags', tags)
        for tag in tags:
            if tag not in shelf.tag_dict.keys():
                des = input('    ' + tag + ' description: ')
                shelf.tag_dict.update({tag: des})

    def delete_recipe(self):
        shelf.delete_recipe(self.id)

    def select_ingredient(self):
        ing_name = input('select which ingredient: ')
        ingredient = [ing for ing in shelf.master_list.ingredients if ing.name == ing_name][0]
        print('-' + ingredient.name)
        ing_interface = IngredientInterface(ingredient.id)
        ing_interface.run()
