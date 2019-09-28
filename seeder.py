from book import Book
from master_db import MasterDB

class Seeder:

    def __init__(self):
        self.seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")

    def refresh_seed(self):
        self.seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")

    def populate_master(self, book_shelf):
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
                    ing_name_list = [item.strip() for item in raw_list if item.strip()] #remove spaces and empty ingredients
                    ingredient_list = []
                    for ing_name in ing_name_list:
                        ingredient_list.append(book_shelf.master_list.find_ing_by_name(ing_name))
                    book_shelf.master_list.add_recipe(comps[0].strip(), comps[1].strip(), ingredient_list)
        return book_shelf

    def populate_books(self, book_shelf):
        active_book = Book("",[])
        for aline in self.seed_file:
            if aline[0] == '*':
                book_shelf.add_book(active_book.name, active_book.recipes)
                comps = aline.split("****")
                active_book.name = comps[1].strip()
                active_book.recipes = []
                active_book.ingredients = []
            elif aline[0] == '=':
                pass
            else:
                if len(aline) > 1 and not aline.isspace():
                    active_book.recipes.append(aline.strip())
        return book_shelf

    def update_seed(self, book_shelf): #TODO fix this for master_db vs recipe_book
        #get ready to write in seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')

        self.write_master_to_seed(book_shelf.master_list, seed_file)

        for book in book_shelf.books:
            seed_file.writelines('**** ' + book.name + ' **** \n')
            #write the ingredients first
            self.write_book_to_seed(book, seed_file)
        seed_file.writelines('******** \n')
        seed_file.close

    def write_master_to_seed(self, book, seed_file):
        seed_file.writelines("===== Ingredients =====\n")
        for item in book.ingredients:
            seed_file.writelines(item.name + ' | ' + item.cost + ' | ' + item.location + ' | \n')
        #then write the recipes
        seed_file.writelines("===== Recipes =====\n")
        for item in book.recipes:
            seed_file.writelines(item.name + ' | ' + item.meal + ' | ') 
            for ingr in item.ingredients: 
                seed_file.writelines(ingr.name + ', ')
            seed_file.writelines(' | \n')

    def write_book_to_seed(self, book, seed_file):
        seed_file.writelines("===== Recipes =====\n")
        for item in book.recipes:
            seed_file.writelines(item + '\n') 
