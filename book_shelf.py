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

    def create_ran_daily_rb(self): 
        random.seed()
        breakfast_recipe = random.choice(self.master_list.find_recipes_by_meal('breakfast'))
        lunch_recipe = random.choice(self.master_list.find_recipes_by_meal('lunch'))
        dinner_recipe = random.choice(self.master_list.find_recipes_by_meal('dinner'))
        recipes = [breakfast_recipe, lunch_recipe, dinner_recipe]
        d = datetime.datetime.today()
        timestamp = d.strftime("%d-%b-%Y (%H:%M:%S)") #.%f
        recipe_book = RecipeBook(timestamp, recipes)
        return recipe_book