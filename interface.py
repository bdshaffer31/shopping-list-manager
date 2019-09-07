from seeder import Seeder
from book_shelf import BookShelf
from confirm import confirm

class Interface:

    def __init__(self):
        self.seeder = Seeder()

    def run(self):
        while(True):
            action = input('input action: ')
            if action == "help":
                print("help \nexit \ndisplay_recipes \ncreate_recipe \ndisplay_by_meal")
            elif action == "display_recipes":
                self.display_recipes()
            elif action == "create_recipe":
                self.create_recipe()
            elif action == "exit":
                break

    def create_recipe(self):
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm("create new recipe")==False: 
            exit()

        self.seeder.refresh_seed()
        shelf = BookShelf() # empty book shelf to fill from seed
        shelf = self.seeder.populate_bookshelf()

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
        pass

    def display_recipes(self):
        print("made it to display recipes")
        #use function confirm() from confirm.py to check if user wants to proceed
        if confirm("view recipe book contents")==False: 
            exit()

        self.seeder.refresh_seed()
        shelf = BookShelf() # empty book shelf to fill from seed
        shelf = self.seeder.populate_bookshelf()

        for rec in shelf.master_list.recipes:
                print("- " + rec.name + " - ", end = "")
                for ing in rec.ingredients:
                    print(ing + ", ", end = "")
                print()
        for book in shelf.recipe_books:
            print("* " + book.name + " * ")
            for rec in book.recipes:
                print("- " + rec.name + " - ", end = "")
                for ing in rec.ingredients:
                    print(ing + ", ", end = "")
                print()

    def edit_recipe(self):
        pass