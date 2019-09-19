from recipe_book import RecipeBook
from master_db import MasterDB
import random
import datetime

class BookShelf:

    def __init__(self):
        self.master_list = MasterDB([], [])
        self.recipe_books = []
              
    def add_recipe_book(self, name, recipes): #TODO add check if recipe already exists
        self.recipe_books.append(RecipeBook(name, recipes)) 

    def change_rec_name(self, old_name, new_name): # shorten using map or list comprehension
        for rec in self.master_list.recipes:
            if rec.name == old_name:
                rec.name = new_name
        for rec_book in self.recipe_books:
            rec_list=[]
            for rec in rec_book.recipes:
                if rec == old_name:
                    rec = new_name
                rec_list.append(rec)
            rec_book.recipes = rec_list

    def change_rec_meal(self, name, new_meal):
        for rec in self.master_list.recipes:
            if rec.name == name:
                rec.meal = new_meal

    def create_ran_daily_rb(self): 
        random.seed()
        breakfast_recipe = random.choice(self.master_list.find_recipes_by_meal('breakfast'))
        lunch_recipe = random.choice(self.master_list.find_recipes_by_meal('lunch'))
        dinner_recipe = random.choice(self.master_list.find_recipes_by_meal('dinner'))
        recipe_names = [breakfast_recipe.name, lunch_recipe.name, dinner_recipe.name]
        d = datetime.datetime.today()
        timestamp = d.strftime("%d-%b-%Y (%H:%M:%S)") #.%f
        recipe_book = RecipeBook(timestamp, recipe_names)
        return recipe_book