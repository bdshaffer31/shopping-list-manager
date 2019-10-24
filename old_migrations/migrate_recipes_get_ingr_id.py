from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from ingredient import Ingredient
from confirm import confirm
from recipe import Recipe
import random
import datetime

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

all_recipes = []

for recipe in shelf.master_list.recipes:
    #print(recipe.ingredients)
    ingr_ids = []
    for ingr in recipe.ingredients:
        for master_ingr in shelf.master_list.ingredients:
            if ingr.name == master_ingr.name:
                ingr_ids.append(master_ingr.id)
        
    all_recipes.append(Recipe(recipe.name, recipe.meal, ingr_ids, recipe.tags))
    #print(recipe.ingredients)

shelf.master_list.recipes = all_recipes
print('done')

shelf.update_db()