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

    def sorted_shopping_list(self, ingr_list):
        ingr_list = sorted(ingr_list, key=lambda ingr: ingr.location )
        return ingr_list
                
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

    def add_ran_daily_plans(self, book, days): 
        recipes = []
        for i in range(days):
            random.seed()
            breakfast_recipe = random.choice(self.master_list.find_recipes_by_meal('breakfast'))
            lunch_recipe = random.choice(self.master_list.find_recipes_by_meal('lunch'))
            dinner_recipe = random.choice(self.master_list.find_recipes_by_meal('dinner'))
            recipes.extend([breakfast_recipe.name, lunch_recipe.name, dinner_recipe.name])
            i
        book.recipes.extend(recipes)
        return book

# make the 'shelf' where whole db will be stored in local memory for duration of program
shelf = BookShelf()
shelf = shelf.populate_bookshelf()