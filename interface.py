from seeder import Seeder
from book_shelf import BookShelf
from confirm import confirm

class Interface:

    def __init__(self):
        self.seeder = Seeder()

    def run(self):
        while(True):
            action = input('input action: ')
            if action == 'help':
                print('help \nexit \ndisplay_recipes \ncreate_recipe \ndisplay_by_meal')
            elif action == 'display_recipes':
                self.display_recipes()
            elif action == 'create_recipe':
                self.create_recipe()
            elif action == 'display_meal':
                self.display_meal()
            elif action == 'exit':
                break
            else:
                print('input not recognized, type \'help\' for a list')

    def create_recipe(self):
        shelf = self.setup_and_seed('create new recipe')

        name = input('enter recipe name: ')
        meal = input('enter recipe meal: ').lower()
        ingrediants = input('enter recipe ingrediants: ')

        ingr_list = ingrediants.split(', ')

        #check if ingredient sharing name exists
        for ingr in ingr_list:
            found = shelf.master_list.find_ingredient(ingr)
            if not found:
                print('new ingredient ' + ingr + ' enter additional info')
                cost = input('enter ingrediant cost: ')
                location = input('enter ingrediant location: ')
                shelf.master_list.add_ingredient(ingr, cost, location)

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
        for book in shelf.recipe_books:
            print("* " + book.name + " * ")
            self.print_recipes(book.recipes)

    def edit_recipe(self):
        pass

    def print_recipes(self, rec_list):
        for rec in rec_list:
            print("- " + rec.name + " - ", end = "")
            for ing in rec.ingredients:
                print(ing + ", ", end = "")
            print()

    def setup_and_seed(self, confirm_message):
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm(confirm_message)==False: 
            exit()
        self.seeder.refresh_seed()
        shelf = self.seeder.populate_bookshelf()
        return shelf