from book import Book
from master_db import MasterDB
from seeder import Seeder
import random
import datetime

class BookShelf:

    def __init__(self):
        self.master_list = MasterDB([], [])
        self.books = []
        self.tag_dict = {}

    def populate_bookshelf(self):
        seeder = Seeder()
        book_shelf = seeder.read_with_pickle()
        return book_shelf

    def update_db(self):
        seeder = Seeder()
        seeder.write_with_pickle(self)  

    def write_for_humans(self): #defunct
        seeder = Seeder()
        seeder.write_for_humans(self)

    def get_book(self, book_id):
        return [x for x in self.books if x.id == book_id][0]
              
    def add_book(self, name, recipes): #TODO add check if recipe already exists
        self.books.append(Book(name, recipes)) 

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)

    def book_ingr_list(self, book_id):
        ingrs = []
        for rec in self.get_book(book_id).recipes:
            ingr_ids = shelf.master_list.rec_ingrs(rec)
            ingrs.extend(shelf.master_list.get(shelf.master_list.ingredients, ingr_ids))
        return ingrs

    def sorted_shopping_list(self, ingr_list):
        ingr_list = sorted(ingr_list, key=lambda ingr: ingr.location )
        return ingr_list
                
    def remove_recipe_from_book(self, book_id, rec_id):
        recs = [rec for rec in self.get_book(book_id).recipes if rec != rec_id]
        self.edit_book_attr(book_id, 'recipes', recs)

    def delete_recipe(self, rec_id):
        for rec in self.master_list.recipes:
            if rec.id == rec_id:
                self.master_list.recipes.remove(rec)
        for book in self.books:
            self.remove_recipe_from_book(book.id, rec_id)

    def edit_book_attr(self, book_id, attribute, new_value):
        setattr(self.get_book(book_id), attribute, new_value)

    def add_by_criteria(self, book_id, number, meal, tags):
        new_recipes = self.ran_select_by_criteria(number, meal, tags)
        for rec in new_recipes: print(' - ' + rec.name)
        rec_ids  = [x.id for x in new_recipes]
        recs = self.get_book(book_id).recipes
        recs.extend(rec_ids)
        self.edit_book_attr(book_id, 'recipes', recs)

    def ran_select_by_criteria(self, number, meal, tags):
        new_recipes = []
        selection = self.master_list.get_by_criteria(meal, tags)
        for i in range(number):
            random.seed()
            new_recipes.append(random.choice(selection))
            i
        return new_recipes
        
    def add_ran_daily_plans(self, book_id, days):
        self.add_by_criteria(book_id, days, 'breakfast', [])
        self.add_by_criteria(book_id, days, 'lunch', [])
        self.add_by_criteria(book_id, days, 'dinner', [])

    # def gen_ran_daily_plans(self, days): 
    #     recipes = []
    #     for i in range(days):
    #         random.seed()
    #         breakfast_recipe = random.choice(self.master_list.get_by_meal('breakfast'))
    #         lunch_recipe = random.choice(self.master_list.get_by_meal('lunch'))
    #         dinner_recipe = random.choice(self.master_list.get_by_meal('dinner'))
    #         recipes.extend([breakfast_recipe, lunch_recipe, dinner_recipe])
    #         i
    #     return recipes

# make the 'shelf' where whole db will be stored in local memory for duration of program
shelf = BookShelf()
shelf = shelf.populate_bookshelf()
