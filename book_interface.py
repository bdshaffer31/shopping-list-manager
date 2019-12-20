# contains the interface for working with a selected recipe book

from book_shelf import BookShelf, shelf
from ingredient import Ingredient
from recipe import Recipe
from confirm import confirm
from ingredient_interface import IngredientInterface
from recipe_interface import RecipeInterface
import mailer

class BookInterface:

    def __init__(self, book_id):
        self.id = book_id

    def run(self):
        self.display()
        commands = {
            'display': self.display,
            'edit name': self.edit_name,
            'add recipes': self.add_recipes,
            'add recipe': self.add_recipe,
            'remove recipe': self.remove_recipe,
            'shopping list': self.gen_shopping_list,
            'add days': self.add_days,
            'add by criteria': self.add_by_criteria,
            'delete book': self.delete_book,
            'select recipe': self.input_select_recipe,
            'exit': shelf.update_db
            }
        while True:
            action = input('input action for ' + self.get_book().name + ': ').strip()
            if action in commands:
                commands[action]()
                if action in ['delete book', 'exit']:
                    break
            elif action == 'help':
                print(' -', end='')
                print(*commands.keys(), sep='\n -')
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

    def add_recipes(self):
        recipes = input('enter recipes to add: ')

        rec_name_list = recipes.split(', ')

        #check if ingredient sharing name exists
        for rec in rec_name_list:
            found = shelf.master_list.find_rec_by_name(rec)
            if not found and rec is not '':
                print('    new recipe, input details')
                meal = input('    enter recipe meal: ').lower().strip()
                tags = input('    enter recipe tags: ').split(', ')

                new_rec = Recipe(rec, meal, [], tags)
                shelf.master_list.recipes.append(new_rec)
                self.get_book().recipes.append(new_rec.id)
                print('    ' + rec + ' added')
            elif found and rec is not '':
                self.get_book().recipes.append(found.id)
                print('    ' + found.name + ' added')
            else:
                print('    invalid recipe name')

    def add_recipe(self): 
        name = input('enter recipe name: ').strip()
        found = shelf.master_list.find_rec_by_name(name)
        if not found and name is not '':
            meal = input('enter recipe meal: ').lower().strip()
            tags = input('enter recipe tags: ').split(', ')

            new_rec = Recipe(name, meal, [], tags)
            shelf.master_list.recipes.append(new_rec)
            self.get_book().recipes.append(new_rec.id)
            self.select_recipe(name)
        elif found:
            self.get_book().recipes.append(found.id)
            print('    ' + found.name + ' added')
            return
        else:
            print('    invalid recipe name')

    def remove_recipe(self):
        recipe_name = input('ingredient to remove: ')
        found = shelf.master_list.find_comp_by_name(recipe_name)
        if found:
            shelf.remove_recipe_from_book(self.id, found.id)
        else:
            print('recipe with name \'' + recipe_name + '\' not found')

    def delete_book(self):
        shelf.delete_book(self.id)

    def gen_shopping_list(self):
        # this is wasteful, looping unneccesary times to sort
        shopping_list = shelf.sorted_shopping_list(shelf.book_ingr_list(self.id))
        shopping_dict = shelf.shopping_dict(shopping_list)
        #ADD write to text file
        for key, value in shopping_dict.items():
            print('    ' + key + ':')
            for ingr in value:
                print('        -' + ingr.name)
        
        send_mail_bool = input('send email (y/n): ')
        if send_mail_bool == 'y':
            self.mail_shop_dict(shopping_dict)

    def mail_shop_dict(self, shopping_dict):
        email_text = mailer.shop_dict_to_string(shopping_dict)
        print(email_text)
        reciever_email = input('send shopping list to: ')
        mailer.send_email(email_text, reciever_email)
        

    def add_by_criteria(self):
        meal = input('get recipes for which meal (any if blank): ')
        tags = input('get recipes for which tags (any if blank): ')
        tags = list(filter(None, tags.split('/')))
        number = int(input('how many recipes to add: '))
        shelf.add_by_criteria(self.id, number, meal, tags)

    def add_days(self):
        days = int(input('how many random days to add: '))
        shelf.add_ran_daily_plans(self.id, days)

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