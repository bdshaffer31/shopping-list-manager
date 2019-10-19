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

    def delete_book(self, name):
        for book in self.books:
            if book.name == name:
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

    def change_rec_name(self, old_name, new_name): # shorten using map or list comprehension
        for rec in self.master_list.recipes:
            if rec.name == old_name:
                rec.name = new_name
        for rec_book in self.books:
            rec_list=[]
            for rec in rec_book.recipes:
                if rec == old_name:
                    rec = new_name
                rec_list.append(rec)
            rec_book.recipes = rec_list

    def remove_ingr_from_recipe(self, recipe_name, ingr_name):
        for rec in self.master_list.recipes:
            if rec.name == recipe_name:
                rec.ingredients = [ingr for ingr in rec.ingredients if ingr.name != ingr_name]

    def change_book_name(self, old_name, new_name): # shorten using map or list comprehension
        for book in self.books:
            if book.name == old_name:
                book.name = new_name
                
    def remove_recipe_from_book(self, book_name, recipe_name):
        for book in self.books:
            if book.name == book_name:
                book.recipes = [rec for rec in book.recipes if rec != recipe_name]

    def change_rec_meal(self, name, new_meal):
        for rec in self.master_list.recipes:
            if rec.name == name:
                rec.meal = new_meal
    
    def add_rec_tags(self, name, tags): #wait why would this be in shelf? => recipe?
        for rec in self.master_list.recipes:
            if rec.name == name:
                rec.tags.extend(tags)

    def delete_recipe(self, rec_name):
        for rec in self.master_list.recipes:
            if rec.name == rec_name:
                self.master_list.recipes.remove(rec)
        for book in self.books:
            self.remove_recipe_from_book(book.name, rec_name)

    def edit_book_attr(self, list, name, attribute, new_value):
        list = [x for x in list if x.name == name]
        setattr(list[0] , attribute, new_value)

    def edit_recipe_attr(self, list, name, attribute, new_value):
        list = [x for x in list if x.name == name]
        setattr(list[0] , attribute, new_value)

    def edit_ingr_attr(self, list, name, attribute, new_value):
        list = [x for x in list if x.name == name]
        setattr(list[0] , attribute, new_value)

    def delete_ingredient(self, ingr_name):
        for ingr in self.master_list.ingredients:
            if ingr.name == ingr_name:
                self.master_list.ingredients.remove(ingr)
        for rec in self.master_list.recipes:
            self.remove_ingr_from_recipe(rec.name, ingr_name)

    def recipes_containing(self, ingr_name):
        pass

    def create_ran_daily_rb(self): 
        random.seed()
        breakfast_recipe = random.choice(self.master_list.find_recipes_by_meal('breakfast'))
        lunch_recipe = random.choice(self.master_list.find_recipes_by_meal('lunch'))
        dinner_recipe = random.choice(self.master_list.find_recipes_by_meal('dinner'))
        recipe_names = [breakfast_recipe.name, lunch_recipe.name, dinner_recipe.name]
        d = datetime.datetime.today()
        timestamp = d.strftime("%d-%b-%Y (%H:%M:%S)") #.%f
        book = Book(timestamp, recipe_names)
        return book

# make the 'shelf' where whole db will be stored in local memory ofr duration of program
shelf = BookShelf()
shelf = shelf.populate_bookshelf()