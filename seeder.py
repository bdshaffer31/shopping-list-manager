from book_shelf import BookShelf
from recipe_book import RecipeBook

class Seeder:

    def __init__(self):
        self.seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")

    def refresh_seed(self):
        self.seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")
        
    def populate_bookshelf(self):
        book_shelf = BookShelf()
        book_shelf = self.populate_master(book_shelf)
        book_shelf = self.populate_recipe_books(book_shelf)
        return book_shelf

    def populate_master(self, book_shelf): # possible to combine with populate recipe book?
        adding_recipes = True
        for aline in self.seed_file:
            if aline[0] == '*':
                break
            elif aline[0] == "=":
                adding_recipes = not adding_recipes
            elif not adding_recipes:
                if len(aline) > 1 and not aline.isspace():
                    comps = aline.split(" | ")
                    book_shelf.master_list.add_ingredient(comps[0], comps[1], comps[2])
            else:
                if len(aline) > 1 and not aline.isspace():
                    comps = aline.split(" | ")
                    raw_list = comps[2].split(',')
                    ingredient_list = [item.strip() for item in raw_list if item.strip()] #remove spaces and empty ingredients
                    book_shelf.master_list.add_recipe(comps[0], comps[1], ingredient_list)
        return book_shelf

    def populate_recipe_books(self, book_shelf): #possible to combine?
        active_book = RecipeBook("",[],[])
        adding_recipes = True
        for aline in self.seed_file:
            if aline[0] == '*':
                book_shelf.add_recipe_book(active_book.name, active_book.recipes, active_book.ingredients)
                comps = aline.split("****")
                active_book.name = comps[1]
                active_book.recipes = []
                active_book.ingredients = []
            elif aline[0] == "=":
                adding_recipes = not adding_recipes
            elif not adding_recipes:
                if len(aline) > 1 and not aline.isspace():
                    comps = aline.split(" | ")
                    active_book.add_ingredient(comps[0], comps[1], comps[2])
            else:
                if len(aline) > 1 and not aline.isspace():
                    comps = aline.split(" | ")
                    raw_list = comps[2].split(',')
                    ingredient_list = [item.strip() for item in raw_list if item.strip()] #remove spaces and empty ingredients
                    active_book.add_recipe(comps[0], comps[1], ingredient_list)
        return book_shelf

    def update_seed(self, book_shelf):# this is all taken from book_shelf and needs to be updated
        #get ready to write in seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')

        self.write_line_to_seed(book_shelf.master_list, seed_file)

        for book in book_shelf.recipe_books:
            seed_file.writelines('**** ' + book.name + ' **** \n')
            #write the ingredients first
            self.write_line_to_seed(book, seed_file)
        seed_file.writelines('******** \n')
        seed_file.close

    def write_line_to_seed(self, book, seed_file):
        seed_file.writelines("===== Ingredients =====\n")
        for item in book.ingredients:
            seed_file.writelines(item.name + ' | ' + item.cost + ' | ' + item.location + ' | \n')
        #then write the recipes
        seed_file.writelines("===== Recipes =====\n")
        for item in book.recipes:
            seed_file.writelines(item.name + ' | ' + item.meal + ' | ') 
            for ingr in item.ingredients: 
                seed_file.writelines(ingr + ', ')
            seed_file.writelines('| \n')
