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

all_books = []
for book in shelf.books:
    all_books.append(Book(book.name, book.recipes))
    #print(book.id)

shelf.books = all_books
all_ingr = []

for ingr in shelf.master_list.ingredients:
    all_ingr.append(Ingredient(ingr.name, ingr.cost, ingr.location, ingr.servings))
    #print(ingr.id)

shelf.master_list.ingredients = all_ingr
all_recipe = []

for recipe in shelf.master_list.recipes:
    all_recipe.append(Recipe(recipe.name, recipe.meal, recipe.ingredients, recipe.tags))
    #print(recipe.id)
shelf.master_list.recipes = all_recipe

print(*shelf.books[2].__dict__)
print(*shelf.master_list.ingredients[3].__dict__)

shelf.update_db()
shelf = shelf.populate_bookshelf()

print(*shelf.books[2].__dict__)
print(*shelf.master_list.ingredients[3].__dict__)

shelf.update_db()