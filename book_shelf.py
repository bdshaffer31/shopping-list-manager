from book import Book
from master_db import MasterDB
from seeder import Seeder
import random
import datetime

class BookShelf:

    def __init__(self):
        self.master_list = MasterDB([], [])
        self.books = []

    def populate_bookshelf(self):
        seeder = Seeder()
        book_shelf = seeder.read_with_pickle()
        return book_shelf

    def update_db(self):
        seeder = Seeder()
        seeder.write_with_pickle(self)  

    def write_for_humans(self):
        seeder = Seeder()
        seeder.write_for_humans(self)
              
    def add_book(self, name, recipes): #TODO add check if recipe already exists
        self.books.append(Book(name, recipes)) 

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)

    def book_ingr_list(self, book):
        ingredients = []
        for rec in book.recipes:
            for mrec in self.master_list.recipes:
                if mrec.name == rec:
                    for ingr in mrec.ingredients:
                        ingredients.append(ingr)
        return ingredients

    def shopping_list(self, ingr_list):
        ingr_list = sorted(ingr_list, key=lambda ingr: ingr.location )
        return ingr_list

    def change_rec_name(self, rec_id, new_name): # shorten using map or list comprehension
        for rec in self.master_list.recipes:
            if rec.id == rec_id:
                rec.name = new_name

    def remove_ingr_from_recipe(self, rec_id, ingr_id):
        for rec in self.master_list.recipes:
            if rec.id == rec_id:
                rec.ingredients = [ingr for ingr in rec.ingredients if ingr.id != ingr_id]

    def change_book_name(self, book_id, new_name): # shorten using map or list comprehension
        for book in self.books:
            if book.id == book_id:
                book.name = new_name
                
    def remove_recipe_from_book(self, book_id, rec_id):
        for book in self.books:
            if book.id == book_id:
                book.recipes = [rec for rec in book.recipes if rec != rec_id]

    def delete_recipe(self, rec_id):
        for rec in self.master_list.recipes:
            if rec.id == rec_id:
                self.master_list.recipes.remove(rec)
        for book in self.books:
            self.remove_recipe_from_book(book.id, rec_id)

    def edit_book_attr(self, list, book_id, attribute, new_value):
        list = [x for x in list if x.id == book_id]
        setattr(list[0] , attribute, new_value)

    def edit_recipe_attr(self, list, rec_id, attribute, new_value):
        list = [x for x in list if x.id == rec_id]
        setattr(list[0] , attribute, new_value)

    def edit_ingr_attr(self, list, ingr_id, attribute, new_value):
        list = [x for x in list if x.id == ingr_id]
        setattr(list[0] , attribute, new_value)

    def delete_ingredient(self, ingr_id):
        for ingr in self.master_list.ingredients:
            if ingr.id == ingr_id:
                self.master_list.ingredients.remove(ingr)
        for rec in self.master_list.recipes:
            self.remove_ingr_from_recipe(rec.id, ingr_id)

    def recipes_containing(self, list, ingr_name):
        pass

    def recipes_with_tag(self, list, tag):
        pass

    def get_ingredients_from_ids(self, ingr_ids):
        ingredients = [x for x in self.master_list.ingredients if x.id in ingr_ids]
        return ingredients     

    def add_ran_daily_plans(self, book, days): 
        recipes = []
        for i in range(days):
            random.seed()
            breakfast_recipe = random.choice(self.master_list.find_recipes_by_meal('breakfast'))
            lunch_recipe = random.choice(self.master_list.find_recipes_by_meal('lunch'))
            dinner_recipe = random.choice(self.master_list.find_recipes_by_meal('dinner'))
            recipes.extend([breakfast_recipe.name, lunch_recipe.name, dinner_recipe.name])
            i
        #d = datetime.datetime.today()
        #timestamp = d.strftime("%d-%b-%Y (%H:%M:%S)") #.%f
        book.recipes.extend(recipes)
        return book

# make the 'shelf' where whole db will be stored in local memory for duration of program
shelf = BookShelf()
shelf = shelf.populate_bookshelf()