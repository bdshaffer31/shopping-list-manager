from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from ingredient import Ingredient
from confirm import confirm
from recipe import Recipe
import random
import datetime

# THIS NEEDS TO BE DONE BUT THIS IS NOT A WORKING MIGRANTION! CAUSED DB CRASH

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

all_books = []
for book in shelf.books:
    all_books.append(Book(book.name, book.recipes))
    #print(book.id)

shelf.books = all_books
all_ingr = []

for ingr in shelf.master_list.ingredients:
    old_id = ingr.id
    new_ingr = Ingredient(ingr.name, ingr.cost, ingr.location, ingr.servings)
    all_ingr.append(new_ingr)
    for recipe in shelf.master_list.recipes:
        for ingr in recipe.ingredients:
            if ingr == old_id:
                ingr = new_ingr.id
    #print(ingr.id)

shelf.master_list.ingredients = all_ingr
all_recipe = []

for recipe in shelf.master_list.recipes:
    old_id = recipe.id
    new_rec = Recipe(recipe.name, recipe.meal, recipe.ingredients, recipe.tags)
    all_ingr.append(new_rec)
    for book in shelf.books:
        for rec in book.recipes:
            if rec == old_id:
                rec = new_rec.id
    #print(recipe.id)
shelf.master_list.recipes = all_recipe

print(*shelf.books[2].__dict__)
print(*shelf.master_list.ingredients[3].__dict__)

shelf.update_db()
shelf = shelf.populate_bookshelf()

print(*shelf.books[2].__dict__)
print(*shelf.master_list.ingredients[3].__dict__)

shelf.update_db()