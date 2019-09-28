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
        seeder.refresh_seed()
        book_shelf = BookShelf()
        book_shelf = seeder.populate_master(book_shelf)
        book_shelf = seeder.populate_books(book_shelf)
        return book_shelf
    
    def update_seed(self):
        seeder = Seeder()
        seeder.update_seed(self)
              
    def add_book(self, name, recipes): #TODO add check if recipe already exists
        self.books.append(Book(name, recipes)) 

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

    def change_ingr_name(self, old_name, new_name): # shorten using map or list comprehension
        for ingr in self.master_list.ingredients:
            if ingr.name == old_name:
                ingr.name = new_name

    def change_book_name(self, old_name, new_name): # shorten using map or list comprehension
        for book in self.books:
            if book.name == old_name:
                book.name = new_name

    def change_rec_meal(self, name, new_meal):
        for rec in self.master_list.recipes:
            if rec.name == name:
                rec.meal = new_meal

    def delete_recipe(self, rec_name):
        for rec in self.master_list.recipes:
            if rec.name == rec_name:
                self.master_list.recipes.remove(rec)

    def change_ingr_cost(self, name, new_cost):
        for ingr in self.master_list.ingredients:
            if ingr.name == name:
                ingr.cost = new_cost

    def change_ingr_location(self, name, new_location):
        for ingr in self.master_list.ingredients:
            if ingr.name == name:
                ingr.location = new_location

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

shelf = BookShelf()
shelf = shelf.populate_bookshelf()