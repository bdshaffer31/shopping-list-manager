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
        self.display()
        commands = { 
            'display': self.display, 
            'detailed display': self.detailed_display,
            'display recipes': self.display_recipes, 
            'display ingrs': self.display_ingredients,
            'display by criteria': self.display_by_criteria,
            'create recipe': self.create_recipe, 
            'select recipe': self.input_select_recipe, 
            'select ingr': self.input_select_ingredient, 
            'create ingr': self.create_ingredients,
            'create book': self.create_book,
            'select book': self.input_select_book,
            'tag dict': self.display_tags,
            'exit': shelf.update_db
            }
        while True:
            action = input('input action: ').strip()
            if action in commands:
                commands[action]()
                if action in ['exit']:
                    #shelf.write_for_humans()
                    break
            elif action == 'help':
                print(' -', end ='')
                print(*commands.keys(), sep = '\n -')
            else:
                print(' -- input not recognized, type \'help\' for a list')

    def display(self):
        for book in shelf.books:
            print(f' - {book.name}')

    def detailed_display(self):
        for book in shelf.books:
            print(' - {book.name}')
            for rec in shelf.get_book(book.id).recipes:
                print(f'    - {shelf.master_list.get(shelf.master_list.recipes, [rec])[0].name}')

    def display_tags(self):
        for key, value in shelf.tag_dict.items():
            print(f'    {key} - {value}')

    def create_recipe(self): 

        name = input('enter recipe name: ').lower().strip()
        found = shelf.master_list.find_rec_by_name(name)
        if not found and name is not '':
            meal = input('enter recipe meal: ').lower().strip()
            tags = input('enter recipe tags: ').lower().split(', ')
            shelf.master_list.add_recipe(name, meal, [], tags)
            self.select_recipe(name)
        elif found:
            print(f'    recipe with name \'{name}\' already exists')
            return
        else:
            print('    invalid recipe name')


    def create_ingredients(self):
        ingredients = input('enter recipe ingrediants: ')
        ingr_name_list = ingredients.split(', ')
        
        for ingr in ingr_name_list:
            #check if ingredient sharing name exists
            found = shelf.master_list.find_ing_by_name(ingr)
            if not found and ingr is not '':
                print(f'new ingredient \'{ingr}\' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                servings = input('enter ingrediant servings: ')
                new_ingr = Ingredient(ingr, cost, location, servings)
                shelf.master_list.ingredients.append(new_ingr)
            elif found and ingr is not '':
                print(f'    ingredient with name \'{ingr}\' already exists')
            else:
                print('    invalid ingredient name')

    def display_recipes(self):
        self.print_recipes(shelf.master_list.recipes)

    def display_ingredients(self):
        for ingr in shelf.master_list.ingredients:
            print(' - ' + ingr.name)

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
            print(f'book with name \'{name}\' not found')
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
            print(f'recipe with name \'{name}\' not found')
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
            print(f'ingredient with name \'{name}\' not found')
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
            for rec in shelf.master_list.get(shelf.master_list.recipes, rec.ingredients):
                print(rec.name + ", ", end = "")
            print()

    def display_by_criteria(self): # is returning union not intersection
        meal = input('get recipes for which meal (any if blank): ')
        tags = input('get recipes for which tags (any if blank): ')
        tags = list(filter(None, tags.split('/')))
        recs = shelf.master_list.get_by_criteria(meal, tags)
        self.print_recipes(recs)

    def display_meal(self): #no longer and option from input
        meal = input('display all recipes for which meal: ')
        rec_list = shelf.master_list.find_recipes_by_meal(meal)
        self.print_recipes(rec_list)

    def display_recipe_costs(self): # no longer and option from input
        self.print_costs(shelf.master_list.recipes)
